from threading import Thread
import cv2

class FaceDetector:

    def __init__(self):

        self.is_frame_changed = False

        self.stopped = False

        # self.frame = frame

        self.ds_factor = 0.7

        self.face_frame = 0

        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def proccess_images_by_threading(self, in_q, out_q, flag_q):

        Thread(target=self.proccess_images, args=(in_q, out_q, flag_q, )).start()
        
        return self

    def proccess_images(self, in_q, out_q, flag_q):

        while not self.stopped:
                
            image = cv2.resize(in_q.get(), None, fx=self.ds_factor, fy=self.ds_factor, interpolation=cv2.INTER_AREA)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            face_rects = self.faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))

            for (x, y, w, h) in face_rects:
                
                ## TO DO -> FLAG MANTIGINI OTURT, X KOORDINAT DEGISIMI  5 PIXELDEN BUYUK OLMADAN QUEUE'YA SOKMA !

                # x_coordinate_flag = out_q.get()

                face_rectangle_query = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                if(flag_q.empty() == True):

                    flag_q.put(face_rects[0])
                    out_q.put(face_rects[0])
                
                else:

                    previous_element_of_flag_queue = flag_q.get()

                    last_position_of_face_x_coordinate = previous_element_of_flag_queue[0]

                    if (abs(face_rects[0][0] - last_position_of_face_x_coordinate)>5):

                        print("ARADAKI FARK 5 OLDU ")

                        flag_q.put(face_rects[0])

                        out_q.put(face_rects[0])

    def stop(self):
        
        self.stopped = True

                # print(type(x_coordinate_flag)
                
                # if (abs(face_rects[0][x] - x_coordinate_flag[2])>5):
                #     # sadece ilk gireni queue'ya sokuyorum
                #     if (len(face_rects)) > 1:

                #         out_q.put(face_rects[0])
 
                #     else:

                #         out_q.put(face_rects[0])

                # self.face_frame = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            