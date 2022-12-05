import time
import serial
import RPi.GPIO as GPIO


TXDEN_2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(TXDEN_2, GPIO.OUT)

GPIO.output(TXDEN_2, GPIO.LOW) 


ser = serial.Serial(
        port='/dev/ttySC1', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser.write(b'\xFF\x01\xAA\x20\x00\x28\xEE')

time.sleep(0.05)

GPIO.output(TXDEN_2, GPIO.HIGH)