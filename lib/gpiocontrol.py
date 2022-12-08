#!/usr/bin/sudo /usr/bin/python3
import time
import sys
import subprocess
from PyQt5.QtCore import Qt

class GpioControl():

    def __init__(self):
        

        try:
            pin1export = open("/sys/class/gpio/export","w")
            pin1export.write("80")
            pin1export.close()
            pin2export = open("/sys/class/gpio/export","w")
            pin2export.write("81")
            pin2export.close()
            pin3export = open("/sys/class/gpio/export","w")
            pin3export.write("82")
            pin3export.close()

            fp1 = open("/sys/class/gpio/gpio80/direction", "w")
            fp1.write( "out" )
            fp1.close()
            fp2 = open("/sys/class/gpio/gpio81/direction", "w")
            fp2.write( "out" )
            fp2.close()
            fp3 = open("/sys/class/gpio/gpio82/direction", "w")
            fp3.write( "out" )
            fp3.close()
            
        except:
            print("INFO: GPIO 3 already exists, skipping export")

        

    def controlRelay1(self, value):

        relay1 = open("/sys/class/gpio/gpio80/value", "w")

        relay1.write(str(value))

        relay1.close()

    def controlRelay2(self, value):

        relay2 = open("/sys/class/gpio/gpio81/value", "w")

        relay2.write(str(value))

        relay2.close()

    def controlRelay3(self, value):

        relay3 = open("/sys/class/gpio/gpio82/value", "w")

        relay3.write(str(value))

        relay3.close()