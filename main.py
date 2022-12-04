import os
import time
import cv2

from lib.video_get import VideoGet
from lib.video_show import VideoShow
from lib.face_detector import FaceDetector
from lib.pelco_ptz_controller import PelcoPtzController

from queue import Queue
from threading import Thread 

def playground():

    stream = cv2.VideoCapture(1)

    stream2 = cv2.VideoCapture(0)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    ptz_controller = PelcoPtzController()

    counter = 0

    while True:

        grabbed, frame = stream.read()

        grabbed2, frame2 = stream2.read()

        image = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.rectangle(image, (260, 180), (380, 300), (0, 0, 0), 2)

        cv2.putText(image, "Pelco Face Tracker", (120, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),1, cv2.LINE_AA)

        cv2.line(image, (320, 220), (320, 260), (0, 0, 255), 3)

        cv2.line(image, (300, 240), (340, 240), (0, 0, 255), 3)

        face_rects = faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(20, 20))

        if (len(face_rects) == 0):
            
            counter +=1
            if(counter == 100):
                ptz_controller.go_to_zero_pan()
                ptz_controller.go_to_zero_tilt()

        elif(len(face_rects) > 1):

            counter = 0

            dummy_time_variable = time.time()

            first_face_x = None
            first_face_y = None

            print("1'den fazla yüz var")

            print(face_rects[1][1])

            for (x, y, w, h) in face_rects:

                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                first_face_x = x + w/2
                first_face_y = y + h/2 

            ptz_controller.new_generation_set_pan_tilt_3(face_x_coordinat, face_y_coordinat)


        elif(len(face_rects) == 1):

            counter = 0

            for (x, y, w, h) in face_rects:

                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                face_x_coordinat = x + w/2
                face_y_coordinat = y + h/2 
            
            ptz_controller.new_generation_set_pan_tilt_3(face_x_coordinat, face_y_coordinat)

        cv2.imshow("Video", image)

        cv2.imshow("Video2", frame2)

        if cv2.waitKey(1) == ord("q"):
            break


def everythingIsThread(source=0):

    video_getter = VideoGet(source).start()

    video_shower = VideoShow(video_getter.frame).start()

    image_processor = FaceDetector(video_getter.frame).start_detect_faces_from_video_capture()

    while True:

        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()

        frame = video_getter.frame

        image_processor.frame = frame

        processed_image = image_processor.face_frame

        video_shower.frame = processed_image

def threadVideoShowandGet(source=0):

    video_getter = VideoGet(source).start()

    video_shower = VideoShow(video_getter.frame).start()

    while True:

        if video_getter.stopped or video_shower.stopped:

            video_shower.stop()
            video_getter.stop()

def main():

    playground()

if __name__ == "__main__":
    main()