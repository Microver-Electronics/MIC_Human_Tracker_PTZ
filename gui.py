
#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QLabel, QWidget, QComboBox
import sys
from PyQt5.QtCore import  QObject, QThread, pyqtSignal # Threading Classes
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import Qt

from gui.mainwindow import Ui_MainWindow

import serial
import os
import sys
import logging

import struct
import psutil
import time
import config
from threading import Thread
from os import getpid

pid = getpid()
# report the pid
print(pid)

import psutil

process = psutil.Process(pid)

process_name = process.name()

print(process_name)

from lib.auxiliary import Auxiliary
from lib.gpiocontrol import GpioControl 

TXDEN_1 = 27
TXDEN_2 = 22

ser_ptz = config.config(dev = "/dev/ttyS0")

ser_laser = config.config(dev = "/dev/ttyS1")

class LaserControl():

    def __init__(self):

        self.aux = Auxiliary()

        self.command_software_version_number = b'\xFF\x01\xAA\x0C\x01\x00\xEE'

        self.command_power_on = b'\xFF\x01\x00\x09\x00\x01\x0B'

        self.command_power_off = b'\xFF\x01\x00\x0B\x00\x01\x0D'

        self.command_reset = b'\xFF\xAA\xEE'

        self.command_led_on = b'\xFF\x01\xAA\x20\x00\x28\xEE'

        self.laser_sync = 'FF'

        self.laser_addr = '01'

        self.laser_set_motor_pos_byte_2 = "AA"

        self.laser_set_motor_pos_byte_3 = "E5"

        self.laser_set_motor_pos_byte_4 = "00"

        self.motor_position = "C8"

        self.laser_set_motor_pos_byte_6 = "EE"

        self.laser_set_output_power_byte_2 = "AA"

        self.laser_set_output_power_byte_3 = "20"

        self.laser_set_output_power_byte_4 = "00"

        self.laser_power = "28"

        self.laser_set_output_power_byte_6 = "EE"

    def send_command_to_laser(self, message):

        if (message == "version"):

            ser_laser.serial.write(self.command_software_version_number)

        elif(message == "changemotorspeed"):

            message_hex_list = [
            self.laser_sync,
            self.laser_addr,
            self.laser_set_motor_pos_byte_2,
            self.laser_set_motor_pos_byte_3,
            self.laser_set_motor_pos_byte_4,
            self.motor_position,
            self.laser_set_motor_pos_byte_6
            ]

            print(message_hex_list)

            ser_laser.serial.write(bytearray.fromhex("".join(message_hex_list)))

        elif(message == "changelaserpower"):

            message_hex_list = [
            self.laser_sync,
            self.laser_addr,
            self.laser_set_output_power_byte_2,
            self.laser_set_output_power_byte_3,
            self.laser_set_output_power_byte_4,
            self.laser_power,
            self.laser_set_output_power_byte_6
            ]

            print(message_hex_list)

            ser_laser.serial.write(bytearray.fromhex("".join(message_hex_list)))

        elif (message == "poweron"):

            ser_laser.serial.write(self.command_power_on)

        elif(message == "poweroff"):

            ser_laser.serial.write(self.command_power_off)

        elif(message == "reset"):

            ser_laser.serial.write(self.command_reset)

        elif(message == "ledon"):

            ser_laser.serial.write(self.command_led_on)

        time.sleep(0.005)

        pass

class PTZCommander():

    def __init__(self):

        self.aux = Auxiliary()

        self.ser_ptz = config.config(dev = "/dev/ttyS0")

        self.ptz_sync = "FF"

        self.ptz_addr = "01"

        self.ptz_right_cmd1 = "00"

        self.ptz_right_cmd2 = "02"

        self.ptz_left_cmd1 = "00"

        self.ptz_left_cmd2 = "04"

        self.pan_speed = "1E"

        self.tilt_speed = "1E"

        self.ptz_up_cmd1 = "00"

        self.ptz_up_cmd2 = "08"

        self.ptz_down_cmd1 = "00"

        self.ptz_down_cmd2 = "10"
        
        self.command_right = b'\xFF\x01\x00\x02\x1E\x00\x21'

        self.command_left = b'\xFF\x01\x00\x04\x1E\x00\x23'

        self.command_stop = b'\xFF\x01\x00\x00\x00\x00\x01'

        self.command_up = b'\xFF\x01\x00\x08\x00\x1E\x27'

        self.command_down = b'\xFF\x01\x00\x10\x00\x1E\x2F'

        self.command_up_right = b'\xFF\x01\x00\x0A\x1E\x1E\x47'

        self.command_up_left = b'\xFF\x01\x00\x0C\x1E\x1E\x49'

        self.command_down_right = b'\xFF\x01\x00\x12\x1E\x1E\x4F'

        self.command_down_left = b'\xFF\x01\x00\x14\x1E\x1E\x51'

        self.test_command = b'\xFF\x01\x00\x4B\x1E\x1E\x88'


        self.ptz_command_zero_pan = b'\xFF\x01\x00\x4B\x00\x00\x4C'

        self.ptz_command_zero_tilt = b'\xFF\x01\x00\x4D\x00\x00\x4E'

    def send_command(self, command):

        self.ser_ptz.serial.write(command)

        return self

    def go_to_zero_pan(self):

        self.send_command(self.ptz_command_zero_pan)


    def go_to_zero_tilt(self):

        self.send_command(self.ptz_command_zero_tilt)

    def send_command_to_pzt(self, command=None, message=None):
        
        if(command == 'right'):

            significant_cmd_list = [self.ptz_addr, self.ptz_right_cmd1, self.ptz_right_cmd2, self.pan_speed, "00"]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_right_cmd1, self.ptz_right_cmd2, self.pan_speed, "00", sum_of_hex_list[2:]]
 
            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'left'):
            
            significant_cmd_list = [self.ptz_addr, self.ptz_left_cmd1, self.ptz_left_cmd2, self.pan_speed, "00"]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_left_cmd1, self.ptz_left_cmd2, self.pan_speed, "00", sum_of_hex_list[2:]]

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'up'):
            
            significant_cmd_list = [self.ptz_addr, self.ptz_up_cmd1, self.ptz_up_cmd2, self.pan_speed, self.tilt_speed]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_up_cmd1, self.ptz_up_cmd2, self.pan_speed, self.tilt_speed, sum_of_hex_list[2:]]


            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'down'):
            
            significant_cmd_list = [self.ptz_addr, self.ptz_down_cmd1, self.ptz_down_cmd2, self.pan_speed, self.tilt_speed]

            sum_of_hex_list = self.aux.sum_of_hex_list_mod256(significant_cmd_list)

            message_hex_list = [self.ptz_sync, self.ptz_addr, self.ptz_down_cmd1, self.ptz_down_cmd2, self.pan_speed, self.tilt_speed, sum_of_hex_list[2:]]

            ser_ptz.serial.write(bytearray.fromhex("".join(message_hex_list)))

        if(command == 'stop'):

            ser_ptz.serial.write(self.command_stop)
            time.sleep(0.005)#Waiting to send

        if(command=="test"):
            ser_ptz.serial.write(message)
            time.sleep(0.005)#Waiting to send

class Worker(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, QLineEdit=None):

        super(QtCore.QThread, self).__init__()

        self.QLineEdit = QLineEdit

        self.is_running = True

        pass

    def run(self):

        self.message_handler()

        pass

    def message_handler(self):

        data = ""

        while True:

            data_ptz = ser_ptz.serial.read().hex()

            data += str(data_ptz)

            self.QLineEdit.setText(data)

    def stop(self):

        self.is_running = False

        self.terminate()

        pass

class PTZQtGUIMainWindow(QMainWindow, Ui_MainWindow, QWidget):

    def __init__(self, parent=None):
        
        self.ptzCommander = PTZCommander()

        self.laserControl = LaserControl()

        self.gpio_control = GpioControl()

        super().__init__(parent)
        
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        self.ui.up_button.clicked.connect(self.send_up_command)
        
        self.ui.down_button.clicked.connect(self.send_down_command)
        
        self.ui.stop_button.clicked.connect(self.send_stop_command)
        
        self.ui.right_button.clicked.connect(self.send_right_command)
        
        self.ui.left_button.clicked.connect(self.send_left_command)

        self.ui.test_button.clicked.connect(self.send_test_command)

        self.ui.autonom_on_button.clicked.connect(self.autonom_mode_on)

        self.ui.autonom_off_button.clicked.connect(self.autonom_mode_off)

        self.ui.go_to_origin_button.clicked.connect(self.go_to_originn)

        self.ui.relay_on_button.clicked.connect(
            lambda: self.send_relay_command(relay_number=1, relay_command=0)
        )

        self.ui.relay_off_button.clicked.connect(
            lambda: self.send_relay_command(relay_number=1, relay_command=1)
        )

        self.ui.relay_on_button_2.clicked.connect(
            lambda: self.send_relay_command(relay_number=2, relay_command=0)
        )

        self.ui.relay_off_button_2.clicked.connect(
            lambda: self.send_relay_command(relay_number=2, relay_command=1)
        )

        self.ui.relay_on_button_3.clicked.connect(
            lambda: self.send_relay_command(relay_number=3, relay_command=0)
        )

        self.ui.relay_off_button_3.clicked.connect(
            lambda: self.send_relay_command(relay_number=3, relay_command=1)
        )

        self.ui.ptz_speed_slider.valueChanged.connect(self.set_pan_speed)

        self.ui.laser_beam_angle_slider.valueChanged.connect(self.set_laser_beam_angle)

        self.ui.laser_motor_position_slider.valueChanged.connect(
            lambda: self.set_motor_position(message="changemotorspeed"))

        self.ui.laser_power_slider.valueChanged.connect(
            lambda: self.drive_laser(message="changelaserpower"))

        self.ui.laser_power_on_button.clicked.connect(
            lambda: self.drive_laser(message="poweron")
        )

        self.ui.laser_power_off_button.clicked.connect(
            lambda: self.drive_laser(message="poweroff")
        )

        self.ui.laser_version_button.clicked.connect(
            lambda: self.drive_laser(message="version")
        )

        self.ui.laser_reset_button.clicked.connect(
            lambda: self.drive_laser(message="reset")
        )

        self.ui.led_max_button.clicked.connect(
            lambda: self.drive_laser(message="ledon")
        )
        
        self.thread = Worker(parent=None, QLineEdit=self.ui.lne_read)

        self.thread.start()



    def go_to_originn(self):

        self.ptzCommander.go_to_zero_pan()
        self.ptzCommander.go_to_zero_tilt()

    def check_pid(self):

        pid_list = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python3' in p.info['name']]
        result = pid_list[0]['pid']
        return(result)

    def autonom_mode_off(self):

        pid = self.check_pid()

        process = psutil.Process(pid)

        process.suspend()

        pass

    def autonom_mode_on(self):

        pid = self.check_pid()

        process = psutil.Process(pid)

        process.resume()

        pass

    def send_relay_command(self, relay_number, relay_command):

        if(relay_number == 1):

            self.gpio_control.controlRelay1(relay_command)

        elif(relay_number == 2):

            self.gpio_control.controlRelay2(relay_command)

        elif(relay_number == 3):

            self.gpio_control.controlRelay3(relay_command)

    def set_laser_power(self):

        slider_value = self.ui.laser_power_slider.value()

        aux = Auxiliary()

        power = round(aux.scale(slider_value, (0, 100), (0, 40)))

        self.laserControl.laser_power = hex(power)[2:]

    def set_motor_position(self, message):

        slider_value = self.ui.laser_power_slider.value()

        aux = Auxiliary()

        position = round(aux.scale(slider_value, (0, 100), (30, 200)))

        self.laserControl.motor_position = hex(position)[2:]

        self.laserControl.send_command_to_laser(message)

    def set_laser_beam_angle(self):

        slider_value = self.ui.laser_beam_angle_slider.value()

        aux = Auxiliary()

        speed = round(aux.scale(slider_value, (0, 100), (30, 200)))

    def set_pan_speed(self):

        slider_value = self.ui.ptz_speed_slider.value()

        aux = Auxiliary()

        speed = round(aux.scale(slider_value, (0, 100), (30, 63)))

        self.ptzCommander.pan_speed = hex(speed)[2:]
        self.ptzCommander.tilt_speed = hex(speed)[2:]


    def drive_laser(self, message):

        laser_control = LaserControl()

        laser_control.send_command_to_laser(message)

    def send_up_command(self):
        
        self.ptzCommander.send_command_to_pzt(command="up")
    
    def send_down_command(self):
        
        self.ptzCommander.send_command_to_pzt(command="down")

    def send_stop_command(self):
        
        self.ptzCommander.send_command_to_pzt(command="stop")
         
    def send_right_command(self):
        
        self.ptzCommander.send_command_to_pzt(command="right")
        
    def send_left_command(self):
        
        self.ptzCommander.send_command_to_pzt(command="left")

    def hexfmt(self, val):
        # this function converts decimal value to 1byte hex value

        return '0x{:02X}'.format(val)

    def send_test_command(self):

        byte2 = self.ui.byte2_lineEdit.text()
 
        byte3 = self.ui.byte3_lineEdit.text()

        byte4 = self.ui.byte4_lineEdit.text()

        byte5 = self.ui.byte5_lineEdit.text()

        byte6 = self.ui.byte6_lineEdit.text()

        byte_list = [byte2, byte3, byte4, byte5 ,byte6]

        byte_to_decimal_list = []  # creating a list for sum function

        [byte_to_decimal_list.append(int(x, 16)) for x in byte_list] # convert hex values to decimal

        byte_list.append(self.hexfmt((sum(byte_to_decimal_list)%256))[2:]) # add the translated value to the bit list as a hex value

        byte_list = ['FF'] + byte_list

        self.ui.bytesum_lineEdit.setText(hex(sum(byte_to_decimal_list)%256)[2:])

        message = bytes.fromhex("".join(byte_list))

        self.ptzCommander.send_command_to_pzt(command="test", message=message)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    app.setApplicationDisplayName("PZT")
    
    mainPage = PTZQtGUIMainWindow()

    mainPage.show()

    sys.exit(app.exec_())