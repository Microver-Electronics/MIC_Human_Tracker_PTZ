import serial
#import RPi.#GPIO as #GPIO

TXDEN_1 = 27
TXDEN_2 = 22

class config(object):
    def __init__(ser, Baudrate = 9600, dev = "/dev/ttyS0"):
        
        ser.dev = dev
        ser.serial = serial.Serial(ser.dev, Baudrate)
        #GPIO.setmode(#GPIO.BCM)
        #GPIO.setwarnings(False)
        #GPIO.setup(TXDEN_1, #GPIO.OUT)
        #GPIO.setup(TXDEN_2, GPIO.OUT)