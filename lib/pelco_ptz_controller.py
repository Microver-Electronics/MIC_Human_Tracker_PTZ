import serial
import config

import RPi.GPIO as GPIO
import time
import lib.auxiliary as aux

from threading import Thread

class PelcoPtzController():

    def __init__(self, *args, **kwargs):

        self.AuxiliaryFunctions = aux.Auxiliary()

        self.ptz_command_slow_up_left = b'\xFF\x01\x00\x0C\x14\x14\x35'

        self.ptz_command_slow_up_right = b'\xFF\x01\x00\x0A\x14\x14\x33'

        self.ptz_command_slow_down_left = b'\xFF\x01\x00\x0C\x14\x14\x3D'

        self.ptz_command_slow_down_right = b'\xFF\x01\x00\x0C\x14\x14\x3B'

        self.ptz_command_slow_right = b'\xFF\x01\x00\x02\x14\x00\x17'

        self.ptz_command_slow_left = b'\xFF\x01\x00\x04\x14\x00\x19'

        self.ptz_command_slow_up = b'\xFF\x01\x00\x08\x00\x14\x1D'

        self.ptz_command_slow_down = b'\xFF\x01\x00\x10\x00\x14\x25'

        self.ptz_command_right = b'\xFF\x01\x00\x02\x1E\x00\x21'

        self.ptz_command_left = b'\xFF\x01\x00\x04\x1E\x00\x23'

        self.ptz_command_stop = b'\xFF\x01\x00\x00\x00\x00\x01'

        self.ptz_command_up = b'\xFF\x01\x00\x08\x00\x1E\x27'

        self.ptz_command_down = b'\xFF\x01\x00\x10\x00\x1E\x2F'

        self.ptz_command_up_right = b'\xFF\x01\x00\x0A\x1E\x1E\x47'

        self.ptz_command_up_left = b'\xFF\x01\x00\x0C\x1E\x1E\x49'

        self.ptz_command_down_right = b'\xFF\x01\x00\x12\x1E\x1E\x4F'

        self.ptz_command_down_left = b'\xFF\x01\x00\x14\x1E\x1E\x51'

        self.ptz_command_zero_pan = b'\xFF\x01\x00\x4B\x00\x00\x4C'

        self.ptz_command_zero_tilt = b'\xFF\x01\x00\x4D\x00\x00\x4E'

        self.ptz_sync = "FF"

        self.ptz_addr = "01"

        self.ptz_set_pan_cmd1 = "00"

        self.ptz_set_pan_cmd2 = "4B"

        self.ptz_set_tilt_cmd1 = ""

        self.ptz_set_tilt_cmd2 = ""

        self.ptz_right_cmd1 = "00"

        self.ptz_right_cmd2 = "02"

        self.ptz_right_cmd_speed = "3F"

        self.ptz_right_cmd_tilt_speed = "00"

        self.ptz_left_cmd1 = ""

        self.ptz_left_cmd2 = ""

        self.ptz_up_cmd1 = ""

        self.ptz_pan_speed = "3F"

        self.ptz_tilt_speed = "3F"

        self.TXDEN_1 = 27
        self.TXDEN_2 = 22

        self.ser = config.config(dev = "/dev/ttySC0")

        self.ser_laser = config.config(dev = "/dev/ttySC1")

    def auto_speed_commander(self, x, y, distance):

        significant_command_list = [self.ptz_addr, ]

        message_hex_type_list = []

    def new_generation_set_pan_tilt_4(self, x, y, distance):

        pass

    def new_generation_set_pan_tilt_3(self, x, y):

        if(y > 180 and y < 380):

            if(x < 260):

                self.send_command(self.ptz_command_left)

            elif(x > 380):

                self.send_command(self.ptz_command_right)

            else:

                self.send_command(self.ptz_command_stop)

        elif( y < 180 ):

            if(x < 260):

                self.send_command(self.ptz_command_up_left)

            elif(x > 380):

                self.send_command(self.ptz_command_up_right)

            else:

                self.send_command(self.ptz_command_up)

        elif( y > 380 ):

            if(x < 260):

                self.send_command(self.ptz_command_down_left)

            elif(x > 380):

                self.send_command(self.ptz_command_down_right)

            else:

                self.send_command(self.ptz_command_down)

    def new_generation_set_pan_tilt_2(self, x, y):

        if(y > 180 and y < 380):

            if(x < 260):

                self.send_command(self.ptz_command_down_left)

            elif(x > 380):

                self.send_command(self.ptz_command_slow_right)

            else:

                self.send_command(self.ptz_command_stop)

        elif( y < 180 ):

            if(x < 260):

                self.send_command(self.ptz_command_slow_up_left)

            elif(x > 380):

                self.send_command(self.ptz_command_slow_up_right)

            else:

                self.send_command(self.ptz_command_slow_up)

        elif( y > 380 ):

            if(x < 260):

                self.send_command(self.ptz_command_down_left)

            elif(x > 380):

                self.send_command(self.ptz_command_down_right)

            else:

                self.send_command(self.ptz_command_slow_down)

    def set_pan_manually(self, x):
        print(x)
        
        if(x < 260):

            self.send_command(self.ptz_command_slow_left)

        elif(x > 380):

            self.send_command(self.ptz_command_slow_right)

        else:

            self.send_command(self.ptz_command_stop)

    def set_pan_tilt_manually(self, x, y):

        if(x<260 and y<180):

            self.send_command(self.ptz_command_slow_up_left)
        
        elif(x<260 and y>300):

            self.send_command(self.ptz_command_slow_down_left)

        elif(x>380 and y>300):

            self.send_command(self.ptz_command_slow_down_right)

        elif(x>380 and y<180):

            self.send_command(self.ptz_command_slow_up_right)

        elif((x>260 and x<380) and (y<180)):

            self.send_command(self.ptz_command_slow_up)

        elif((x>260 and x<380) and (y>300)):

            self.send_command(self.ptz_command_slow_down)

        elif((x>260) and (y>180 and y<300)):

            self.send_command(self.ptz_command_slow_left)

        elif((x>380) and (y>180 and y<300)):

            self.send_command(self.ptz_command_slow_right)

        else:

            self.send_command(self.ptz_command_stop)

        print(x, y)

    def send_control_command(self):

        self.send_command(self.ptz_command_slow_left)

    def send_command(self, command):
        GPIO.setup(self.TXDEN_1, GPIO.OUT)
        GPIO.output(self.TXDEN_1, GPIO.LOW)

        self.ser.serial.write(command)

        time.sleep(0.005) #Waiting to send

        GPIO.output(self.TXDEN_1, GPIO.HIGH)
        
        return self

    def send_up_command(self):
        GPIO.setup(TXDEN_1, GPIO.OUT)
        GPIO.output(self.TXDEN_1, GPIO.LOW)

        self.ser.serial.write(self.ptz_command_up)

        time.sleep(0.005) #Waiting to send

        GPIO.output(self.TXDEN_1, GPIO.HIGH)
        
        return self

    def send_down_command(self):
        GPIO.setup(TXDEN_1, GPIO.OUT)
        GPIO.output(self.TXDEN_1, GPIO.LOW)

        self.ser.serial.write(self.ptz_command_down)

        time.sleep(0.005) #Waiting to send

        GPIO.output(self.TXDEN_1, GPIO.HIGH)
        
        return self

    def send_right_command(self):
        GPIO.setup(TXDEN_1, GPIO.OUT)
        GPIO.output(self.TXDEN_1, GPIO.LOW)

        self.ser.serial.write(self.ptz_command_right)

        time.sleep(0.005) #Waiting to send

        GPIO.output(self.TXDEN_1, GPIO.HIGH)
        
        return self

    def send_stop_command(self):
        GPIO.setup(self.TXDEN_1, GPIO.OUT)
        GPIO.output(self.TXDEN_1, GPIO.LOW)

        self.ser.serial.write(self.ptz_command_stop)

        time.sleep(0.005) #Waiting to send

        GPIO.output(self.TXDEN_1, GPIO.HIGH)

        return self

    def send_left_command(self):
        GPIO.setup(TXDEN_1, GPIO.OUT)
        GPIO.output(self.TXDEN_1, GPIO.LOW)

        self.ser.serial.write(self.ptz_command_left)

        time.sleep(0.005) #Waiting to send

        GPIO.output(self.TXDEN_1, GPIO.HIGH)

        return self

    def go_tilt_to_the_face(self, y_value):
        GPIO.setup(TXDEN_1, GPIO.OUT)
        y_coordinat = y_value

        if(y_coordinat > 300):

            self.send_down_command()

        elif(y_coordinat < 200):

            self.send_up_command()

        else:

            self.send_stop_command()


    def new_generation_set_pan_position(self, x_position, flag_q):
        GPIO.setup(self.TXDEN_1, GPIO.OUT)
        if( flag_q.empty() == True):

            flag_q.put(x_position)

        else :

            previous_x_position = flag_q.get()

            if (previous_x_position == x_position):

                    pass

            else :

                flag_q.put(x_position)

                pan_degree = self.AuxiliaryFunctions.scale(x_position, (0, 640), (-3000, 4000))

                previous_pan_degree = self.AuxiliaryFunctions.scale(previous_x_position , (0, 1280), (-2000, 3000))

                print(pan_degree)
 
                if pan_degree < 0:

                    degree_hex = self.AuxiliaryFunctions.hexfmt(round(36000 + pan_degree - previous_pan_degree))

                elif pan_degree > 0:

                    degree_hex = self.AuxiliaryFunctions.hexfmt(round(pan_degree - previous_pan_degree))

                else:

                    degree_hex = self.AuxiliaryFunctions.hexfmt(round(pan_degree - previous_pan_degree))

                significant_cmd_list = [self.ptz_addr, self.ptz_set_pan_cmd1, self.ptz_set_pan_cmd2, degree_hex[2:4], degree_hex[4:6]]

                sum_of_hex_list = self.AuxiliaryFunctions.sum_of_hex_list_mod256(significant_cmd_list)

                message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_set_pan_cmd1, self.ptz_set_pan_cmd2, degree_hex[2:4], degree_hex[4:6], sum_of_hex_list[2:]]

                GPIO.output(self.TXDEN_1, GPIO.LOW)

                self.ser.serial.write(bytearray.fromhex("".join(message_hex_list)))

        return self

    def send_set_pan_command_to_ptz(self, in_q, flag_q):
        GPIO.setup(TXDEN_1, GPIO.OUT)
        while True:

            x_degree = in_q.get()

            if (flag_q.empty() == True):

                flag_q.put(x_degree)

            else :

                previous_x_position = flag_q.get()[0]

                if (previous_x_position == x_degree[0]):

                    pass

                else:

                    flag_q.put(x_degree)

                    pan_degree = self.AuxiliaryFunctions.scale(x_degree[0], (0, 1280), (-4500, 4500))

                    previous_pan_degree = self.AuxiliaryFunctions.scale(previous_x_position, (0, 1280), (-2000, 3000))

                    print(pan_degree)
 
                    if pan_degree < 0:

                        degree_hex = self.AuxiliaryFunctions.hexfmt(round(36000 + pan_degree ))

                    elif pan_degree > 0:

                        degree_hex = self.AuxiliaryFunctions.hexfmt(round(pan_degree ))

                    else:

                        degree_hex = self.AuxiliaryFunctions.hexfmt(round(pan_degree ))

                    significant_cmd_list = [self.ptz_addr, self.ptz_set_pan_cmd1, self.ptz_set_pan_cmd2, degree_hex[2:4], degree_hex[4:6]]

                    sum_of_hex_list = self.AuxiliaryFunctions.sum_of_hex_list_mod256(significant_cmd_list)

                    message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_set_pan_cmd1, self.ptz_set_pan_cmd2, degree_hex[2:4], degree_hex[4:6], sum_of_hex_list[2:]]

                    GPIO.output(self.TXDEN_1, GPIO.LOW)

                    self.ser.serial.write(bytearray.fromhex("".join(message_hex_list)))

        return self

    def send_command_to_laser():

        GPIO.setup(self.TXDEN_2, GPIO.OUT)

        GPIO.output(TXDEN_1, GPIO.LOW) 

        self.ser_laser.serial.write(b'\xFF\x01\x00\x09\x00\x01\x0B')

        time.sleep(0.05)

        GPIO.output(self.TXDEN_2, GPIO.HIGH)


        pass

    def go_to_zero_pan(self):

        self.send_command(self.ptz_command_zero_pan)

        pass

    def go_to_zero_tilt(self):

        self.send_command(self.ptz_command_zero_tilt)

        pass

    def send_command_to_pzt(self, command=None, message=None):
        
        if(command == 'right'):

            significant_cmd_list = [self.ptz_addr, self.ptz_right_cmd1, self.ptz_right_cmd2, self.pan_speed, "00"]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_right_cmd1, self.ptz_right_cmd2, self.pan_speed, "00", sum_of_hex_list[2:]]
        
            GPIO.setup(TXDEN_1, GPIO.OUT)
            GPIO.output(TXDEN_1, GPIO.LOW)

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'left'):
            
            significant_cmd_list = [self.ptz_addr, self.ptz_left_cmd1, self.ptz_left_cmd2, self.pan_speed, "00"]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_left_cmd1, self.ptz_left_cmd2, self.pan_speed, "00", sum_of_hex_list[2:]]
        
            GPIO.setup(TXDEN_1, GPIO.OUT)
            GPIO.output(TXDEN_1, GPIO.LOW)

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'up'):
            
            significant_cmd_list = [self.ptz_addr, self.ptz_up_cmd1, self.ptz_up_cmd2, self.pan_speed, self.tilt_speed]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_up_cmd1, self.ptz_up_cmd2, self.pan_speed, self.tilt_speed, sum_of_hex_list[2:]]
        
            GPIO.setup(TXDEN_1, GPIO.OUT)
            GPIO.output(TXDEN_1, GPIO.LOW)

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'down'):
            
            significant_cmd_list = [self.ptz_addr, self.ptz_down_cmd1, self.ptz_down_cmd2, self.pan_speed, self.tilt_speed]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_down_cmd1, self.ptz_down_cmd2, self.pan_speed, self.tilt_speed, sum_of_hex_list[2:]]
        
            GPIO.setup(TXDEN_1, GPIO.OUT)
            GPIO.output(TXDEN_1, GPIO.LOW)

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'stop'):
            GPIO.setup(TXDEN_1, GPIO.OUT)
            GPIO.output(TXDEN_1, GPIO.LOW) 
            ser_ptz.serial.write(self.command_stop)
            time.sleep(0.005)#Waiting to send
            GPIO.output(TXDEN_1, GPIO.HIGH)

        if(command=="test"):
            GPIO.setup(TXDEN_1, GPIO.OUT)
            GPIO.output(TXDEN_1, GPIO.LOW) 
            ser_ptz.serial.write(message)
            time.sleep(0.005)#Waiting to send
            GPIO.output(TXDEN_1, GPIO.HIGH)