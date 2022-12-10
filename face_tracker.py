import os
import time
import cv2
from lib.video_get import VideoGet
from lib.video_show import VideoShow
from lib.face_detector import FaceDetector
from lib.pelco_ptz_controller import PelcoPtzController
from queue import Queue
from threading import Thread 

from flask import Flask, render_template,  Response

import numpy as np

app = Flask(__name__)

frame = Queue()

def playground():

    stream = cv2.VideoCapture(0)

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    ptz_controller = PelcoPtzController()

    counter = 0

    while True:

        grabbed, frame = stream.read()

        #grabbed2, frame2 = stream2.read()

        image = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.rectangle(image, (260, 180), (380, 300), (0, 0, 0), 2)

        cv2.putText(image, "Pelco Face Tracker", (120, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),1, cv2.LINE_AA)

        cv2.line(image, (320, 220), (320, 260), (0, 0, 255), 3)

        cv2.line(image, (300, 240), (340, 240), (0, 0, 255), 3)

        face_rects = faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(20, 20))

        if (len(face_rects) == 0):

            counter +=1
            if(counter == 60):

                ptz_controller.go_to_zero_pan()
                ptz_controller.go_to_zero_tilt()

        elif(len(face_rects) > 1):

            counter = 0

            first_face_x = None
            first_face_y = None
            print("1'den fazla yüz var")

            for (x, y, w, h) in face_rects:

                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                first_face_x = x + w/2
                first_face_y = y + h/2 

            for i in face_rects:

                f= np.unravel_index(i.argmax(), i.shape)

                #max_index = i.index(max(i))

            ptz_controller.new_generation_set_pan_tilt_3(face_x_coordinat, face_y_coordinat)

        elif(len(face_rects) == 1):
            counter = 0

            for (x, y, w, h) in face_rects:

                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                face_x_coordinat = x + w/2
                face_y_coordinat = y + h/2 
            
            ptz_controller.new_generation_set_pan_tilt_3(face_x_coordinat, face_y_coordinat)

        ret, buffer = cv2.imencode('.jpg', image)
        web_frame = buffer.tobytes()

        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + web_frame + b'\r\n')

        cv2.imshow("Video", image)

        #cv2.imshow("Video2", frame2)

        if cv2.waitKey(1) == ord("q"):
            break


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(playground(), mimetype='multipart/x-mixed-replace; boundary=frame')

def main():

    #playground()

    app.run(debug=True)

if __name__ == "__main__":
    main()