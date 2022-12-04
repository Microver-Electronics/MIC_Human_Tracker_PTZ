from threading import Thread
import cv2

class VideoGet():
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)

        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self, out_q):

        Thread(target=self.get, args=(out_q, ), daemon=False).start()
        return self

    def get(self, out_q):
        while not self.stopped:
            if not self.grabbed:
                self.stop()

            else:
                (self.grabbed, self.frame) = self.stream.read()
                
                out_q.put(self.frame)

    def stop(self):
        self.stopped = True