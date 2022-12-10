import serial

class config(object):
    def __init__(ser, Baudrate = 9600, dev = "/dev/ttyS0"):

        ser.dev = dev
        ser.serial = serial.Serial(ser.dev, Baudrate)