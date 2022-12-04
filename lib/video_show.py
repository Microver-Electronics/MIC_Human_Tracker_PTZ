from threading import Thread
import cv2

class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):

        self.frame = frame
        self.stopped = False

    def start(self, in_q):

        Thread(target=self.show, args=(in_q, )).start()
        return self

    def show(self, in_q):

        while not self.stopped:
            cv2.imshow("Video", in_q.get())
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True
