#!/home/microver/Github/MIC_PELCO_FACE_TRACKER/ptzenv/bin/python3

## Microver Electronics 12/30/2022
## Pelco Human Tracker


## Custom python modules
from lib.pelco_ptz_controller import PelcoPtzController
from lib.gpiocontrol import GpioControl
from centroidtracker import CentroidTracker

import cv2
import datetime
import imutils
import numpy as np

from os import getpid

from queue import Queue
from threading import Thread

protopath = "/home/microver/Github/MIC_PELCO_FACE_TRACKER/MobileNetSSD_deploy.prototxt"
modelpath = "/home/microver/Github/MIC_PELCO_FACE_TRACKER/MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)
# Only enable it if you are using OpenVino environment
# detector.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
# detector.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

tracker = CentroidTracker(maxDisappeared=30, maxDistance=90)

def non_max_suppression_fast(boxes, overlapThresh):
    try:
        if len(boxes) == 0:
            return []

        if boxes.dtype.kind == "i":
            boxes = boxes.astype("float")

        pick = []

        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]

        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        idxs = np.argsort(y2)

        while len(idxs) > 0:
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)

            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])

            w = np.maximum(0, xx2 - xx1)
            h = np.maximum(0, yy2 - yy1)

            overlap = (w * h) / area[idxs[:last]]

            idxs = np.delete(idxs, np.concatenate(([last],
                                                   np.where(overlap > overlapThresh)[0])))

        return boxes[pick].astype("int")
    except Exception as e:
        print("Exception occurred in non_max_suppression : {}".format(e))

def playground():
    cap = cv2.VideoCapture(0)

    ptz_controller = PelcoPtzController()

    counter = 0

    while True:

        ret, frame = cap.read()

        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        (H, W) = frame.shape[:2]
        print(W, H)
        rect_const = 105
        rect_pos_start_x = int(((W / 2) - rect_const))
        rect_pos_end_x = int(((W / 2) + rect_const))
        rect_pos_start_y = int(((H / 2) - rect_const / 2))
        rect_pos_end_y = int(((H / 2) + rect_const / 2))

        cv2.rectangle(frame, (rect_pos_start_x, rect_pos_start_y), (rect_pos_end_x, rect_pos_end_y), (0, 0, 0), 1)

        blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

        detector.setInput(blob)
        person_detections = detector.forward()

        rects = []
        for i in np.arange(0, person_detections.shape[2]):
            confidence = person_detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(person_detections[0, 0, i, 1])

                if CLASSES[idx] != "person":
                    continue

                person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])

                (startX, startY, endX, endY) = person_box.astype("int")

                center_x = startX + ((endX - startX) / 2)
                center_y = startY + ((endY - startY) / 2)

                print("Center X : ", center_x, "Center Y : ", center_y, "Screen Width : ", W, " Screen Height : ", H)
                print("Takip Ediyor")

                rects.append(person_box)

        if (len(rects) == 0):

            counter += 1
            print("Takip Etmiyor")
            if (counter == 40):
                ptz_controller.go_to_zero_pan()
                ptz_controller.go_to_zero_tilt()

        elif (len(rects) >= 1):
            counter = 0

            (startX, startY, endX, endY) = rects[0]
            print(startX, startY, endX, endY)

            center_x = startX + ((endX - startX) / 2)
            center_y = startY + ((endY - startY) / 2)

            distance_from_origin_x = abs((W / 2) - center_x)

            distance_from_origin_y = abs((H / 2) - center_y)

            distance_from_origin = distance_from_origin_x + distance_from_origin_y

            ptz_controller.new_generation_set_pan_tilt_3(distance_from_origin, center_x, center_y, rect_pos_start_x,
                                                         rect_pos_start_y, rect_pos_end_x, rect_pos_end_y)

        boundingboxes = np.array(rects)
        boundingboxes = boundingboxes.astype(int)
        rects = non_max_suppression_fast(boundingboxes, 0.1)

        objects = tracker.update(rects)
        for (objectId, bbox) in objects.items():
            x1, y1, x2, y2 = bbox
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            text = "ID: {}".format(objectId)
            cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

        cv2.imshow("Application", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

def main():
    playground()


if __name__ == "__main__":
    main()
