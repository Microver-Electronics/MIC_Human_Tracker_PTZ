import serial
import config

import time
import lib.auxiliary as aux
import time
from threading import Thread
from lib.gpiocontrol import GpioControl

class PelcoPtzController():

    def __init__(self, *args, **kwargs):
        self.AuxiliaryFunctions = aux.Auxiliary()

        self.gpioController = GpioControl()

        self.ptz_command_stop = b'\xFF\x01\x00\x00\x00\x00\x01'

        ### SLOW

        self.ptz_command_slow_up_left = b'\xFF\x01\x00\x0C\x14\x14\x35'

        self.ptz_command_slow_up_right = b'\xFF\x01\x00\x0A\x14\x14\x33'

        self.ptz_command_slow_down_left = b'\xFF\x01\x00\x0C\x14\x14\x3D'

        self.ptz_command_slow_down_right = b'\xFF\x01\x00\x12\x14\x14\x3B'

        self.ptz_command_slow_right = b'\xFF\x01\x00\x02\x14\x00\x17'

        self.ptz_command_slow_left = b'\xFF\x01\x00\x04\x14\x00\x19'

        self.ptz_command_slow_up = b'\xFF\x01\x00\x08\x00\x14\x1D'

        self.ptz_command_slow_down = b'\xFF\x01\x00\x10\x00\x14\x25'

        ### NORMAL SPEED

        self.ptz_command_right = b'\xFF\x01\x00\x02\x1E\x00\x21'

        self.ptz_command_left = b'\xFF\x01\x00\x04\x1E\x00\x23'

        self.ptz_command_up = b'\xFF\x01\x00\x08\x00\x1E\x27'

        self.ptz_command_down = b'\xFF\x01\x00\x10\x00\x1E\x2F'

        self.ptz_command_up_right = b'\xFF\x01\x00\x0A\x1E\x1E\x47'

        self.ptz_command_up_left = b'\xFF\x01\x00\x0C\x1E\x1E\x49'

        self.ptz_command_down_right = b'\xFF\x01\x00\x12\x1E\x1E\x4F'

        self.ptz_command_down_left = b'\xFF\x01\x00\x14\x1E\x1E\x51'

        ### MEDIUM SPEED

        self.ptz_command_medium_right = b'\xFF\x01\x00\x02\x23\x00\x26'

        self.ptz_command_medium_left = b'\xFF\x01\x00\x04\x23\x00\x28'

        self.ptz_command_medium_up = b'\xFF\x01\x00\x08\x00\x23\x2C'

        self.ptz_command_medium_down = b'\xFF\x01\x00\x10\x00\x23\x34'

        self.ptz_command_medium_up_right = b'\xFF\x01\x00\x0A\x23\x23\x51'

        self.ptz_command_medium_up_left = b'\xFF\x01\x00\x0C\x23\x23\x53'

        self.ptz_command_medium_down_right = b'\xFF\x01\x00\x12\x23\x23\x59'

        self.ptz_command_medium_down_left = b'\xFF\x01\x00\x14\x23\x23\x5B'

        ### MAX SPEED

        self.ptz_command_speed_left = b'\xFF\x01\x00\x04\x28\x00\x2D'

        self.ptz_command_speed_right = b'\xFF\x01\x00\x02\x28\x00\x2B'

        self.ptz_command_speed_up = b'\xFF\x01\x00\x08\x00\x28\x31'

        self.ptz_command_speed_down = b'\xFF\x01\x00\x10\x00\x28\x39'

        self.ptz_command_speed_up_right = b'\xFF\x01\x00\x0A\x28\x28\x5B'

        self.ptz_command_speed_up_left = b'\xFF\x01\x00\x0C\x28\x28\x5D'

        self.ptz_command_speed_down_right = b'\xFF\x01\x00\x12\x28\x28\x63'

        self.ptz_command_speed_down_left = b'\xFF\x01\x00\x14\x28\x28\x65'

        ### ZERO

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

        self.ser = config.config(dev="/dev/ttyS0")

        self.ser_laser = config.config(dev="/dev/ttyS1")

    def auto_speed_commander(self, x, y, distance):

        significant_command_list = [self.ptz_addr, ]

        message_hex_type_list = []

    def new_generation_set_pan_tilt_3(self, distance_from_origin, x, y, rect_start_x, rect_start_y, rect_end_x,
                                      rect_end_y):

        speed_control = round(self.AuxiliaryFunctions.scale(distance_from_origin, (0, 384), (1, 4)))

        print("Uzaklik", distance_from_origin)

        # if the person distance is smaller than 60 pixel, shoot!
        if (distance_from_origin < 60):

            self.gpioController.controlRelay2(0)

            time.sleep(0.2)

            self.gpioController.controlRelay2(1)

            time.sleep(0.2)

        elif (distance_from_origin >= 60):

            self.gpioController.controlRelay2(1)  # stop laser

        print(speed_control)

        if (speed_control == 1):

            if (y > rect_start_y and y < rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_slow_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_slow_right)

                else:

                    self.send_command(self.ptz_command_stop)

            elif (y < rect_start_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_slow_up_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_slow_up_right)

                else:

                    self.send_command(self.ptz_command_slow_up)

            elif (y > rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_slow_down_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_slow_down_right)

                else:

                    self.send_command(self.ptz_command_slow_down)

        elif (speed_control == 2):

            if (y > rect_start_y and y < rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_right)

                else:

                    self.send_command(self.ptz_command_stop)

            elif (y < rect_start_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_up_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_up_right)

                else:

                    self.send_command(self.ptz_command_up)

            elif (y > rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_down_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_down_right)

                else:

                    self.send_command(self.ptz_command_down)

        elif (speed_control == 3):

            if (y > rect_start_y and y < rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_medium_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_medium_right)

                else:

                    self.send_command(self.ptz_command_stop)

            elif (y < rect_start_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_medium_up_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_medium_up_right)

                else:

                    self.send_command(self.ptz_command_medium_up)

            elif (y > rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_medium_down_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_medium_down_right)

                else:

                    self.send_command(self.ptz_command_medium_down)

        elif (speed_control == 4):

            if (y > rect_start_y and y < rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_speed_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_speed_right)

                else:

                    self.send_command(self.ptz_command_stop)

            elif (y < rect_start_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_speed_up_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_speed_up_right)

                else:

                    self.send_command(self.ptz_command_speed_up)

            elif (y > rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_speed_down_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_speed_down_right)

                else:

                    self.send_command(self.ptz_command_speed_down)

        else:

            if (y > rect_start_y and y < rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_speed_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_speed_right)

                else:

                    self.send_command(self.ptz_command_stop)

            elif (y < rect_start_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_speed_up_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_speed_up_right)

                else:

                    self.send_command(self.ptz_command_speed_up)

            elif (y > rect_end_y):

                if (x < rect_start_x):

                    self.send_command(self.ptz_command_speed_down_left)

                elif (x > rect_end_x):

                    self.send_command(self.ptz_command_speed_down_right)

                else:

                    self.send_command(self.ptz_command_speed_down)

    def send_command(self, command):

        self.ser.serial.write(command)

        return self

    def send_up_command(self):

        self.ser.serial.write(self.ptz_command_up)

        return self

    def send_down_command(self):

        self.ser.serial.write(self.ptz_command_down)

        time.sleep(0.005)  # Waiting to send

        return self

    def send_right_command(self):

        self.ser.serial.write(self.ptz_command_right)

        time.sleep(0.005)  # Waiting to send

        return self

    def send_stop_command(self):

        self.ser.serial.write(self.ptz_command_stop)

        time.sleep(0.005)  # Waiting to send

        return self

    def send_left_command(self):

        self.ser.serial.write(self.ptz_command_left)

        time.sleep(0.005)  # Waiting to send

        return self

    def send_set_pan_command_to_ptz(self, in_q, flag_q):
        # GPIO.setup(TXDEN_1, #GPIO.OUT)
        while True:

            x_degree = in_q.get()

            if (flag_q.empty() == True):

                flag_q.put(x_degree)

            else:

                previous_x_position = flag_q.get()[0]

                if (previous_x_position == x_degree[0]):

                    pass

                else:

                    flag_q.put(x_degree)

                    pan_degree = self.AuxiliaryFunctions.scale(x_degree[0], (0, 1280), (-4500, 4500))

                    previous_pan_degree = self.AuxiliaryFunctions.scale(previous_x_position, (0, 1280), (-2000, 3000))

                    print(pan_degree)

                    if pan_degree < 0:

                        degree_hex = self.AuxiliaryFunctions.hexfmt(round(36000 + pan_degree))

                    elif pan_degree > 0:

                        degree_hex = self.AuxiliaryFunctions.hexfmt(round(pan_degree))

                    else:

                        degree_hex = self.AuxiliaryFunctions.hexfmt(round(pan_degree))

                    significant_cmd_list = [self.ptz_addr, self.ptz_set_pan_cmd1, self.ptz_set_pan_cmd2,
                                            degree_hex[2:4], degree_hex[4:6]]

                    sum_of_hex_list = self.AuxiliaryFunctions.sum_of_hex_list_mod256(significant_cmd_list)

                    message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_set_pan_cmd1, self.ptz_set_pan_cmd2,
                                        degree_hex[2:4], degree_hex[4:6], sum_of_hex_list[2:]]

                    # GPIO.output(self.TXDEN_1, #GPIO.LOW)

                    self.ser.serial.write(bytearray.fromhex("".join(message_hex_list)))

        return self

    def send_command_to_laser():

        self.ser_laser.serial.write(b'\xFF\x01\x00\x09\x00\x01\x0B')

        time.sleep(0.05)

    def go_to_zero_pan(self):

        self.send_command(self.ptz_command_zero_pan)

    def go_to_zero_tilt(self):

        self.send_command(self.ptz_command_zero_tilt)

    def send_command_to_pzt(self, command=None, message=None):

        if (command == 'right'):
            significant_cmd_list = [self.ptz_addr, self.ptz_right_cmd1, self.ptz_right_cmd2, self.pan_speed, "00"]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_right_cmd1, self.ptz_right_cmd2, self.pan_speed,
                                "00", sum_of_hex_list[2:]]

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if (command == 'left'):
            significant_cmd_list = [self.ptz_addr, self.ptz_left_cmd1, self.ptz_left_cmd2, self.pan_speed, "00"]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_left_cmd1, self.ptz_left_cmd2, self.pan_speed,
                                "00", sum_of_hex_list[2:]]

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if (command == 'up'):
            significant_cmd_list = [self.ptz_addr, self.ptz_up_cmd1, self.ptz_up_cmd2, self.pan_speed, self.tilt_speed]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_up_cmd1, self.ptz_up_cmd2, self.pan_speed,
                                self.tilt_speed, sum_of_hex_list[2:]]

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if (command == 'down'):
            significant_cmd_list = [self.ptz_addr, self.ptz_down_cmd1, self.ptz_down_cmd2, self.pan_speed,
                                    self.tilt_speed]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_down_cmd1, self.ptz_down_cmd2, self.pan_speed,
                                self.tilt_speed, sum_of_hex_list[2:]]

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if (command == 'stop'):
            ser_ptz.serial.write(self.command_stop)

        if (command == "test"):
            ser_ptz.serial.write(message)
