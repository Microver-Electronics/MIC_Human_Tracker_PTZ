# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.left_button = QtWidgets.QPushButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(360, 250, 91, 30))
        self.left_button.setObjectName("left_button")
        self.up_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_button.setGeometry(QtCore.QRect(460, 210, 91, 30))
        self.up_button.setObjectName("up_button")
        self.right_button = QtWidgets.QPushButton(self.centralwidget)
        self.right_button.setGeometry(QtCore.QRect(560, 250, 91, 30))
        self.right_button.setObjectName("right_button")
        self.down_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_button.setGeometry(QtCore.QRect(460, 290, 91, 30))
        self.down_button.setObjectName("down_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(460, 250, 91, 30))
        self.stop_button.setObjectName("stop_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 500, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.test_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_button.setGeometry(QtCore.QRect(120, 270, 111, 30))
        self.test_button.setObjectName("test_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 174, 251, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.byte2_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.byte2_lineEdit.setEnabled(False)
        self.byte2_lineEdit.setObjectName("byte2_lineEdit")
        self.verticalLayout_9.addWidget(self.byte2_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.byte3_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.byte3_lineEdit.setObjectName("byte3_lineEdit")
        self.verticalLayout_8.addWidget(self.byte3_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.byte4_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.byte4_lineEdit.setObjectName("byte4_lineEdit")
        self.verticalLayout_7.addWidget(self.byte4_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.byte5_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.byte5_lineEdit.setObjectName("byte5_lineEdit")
        self.verticalLayout_5.addWidget(self.byte5_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.byte6_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.byte6_lineEdit.setObjectName("byte6_lineEdit")
        self.verticalLayout_4.addWidget(self.byte6_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.bytesum_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.bytesum_lineEdit.setEnabled(False)
        self.bytesum_lineEdit.setObjectName("bytesum_lineEdit")
        self.verticalLayout_2.addWidget(self.bytesum_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 190, 31, 22))
        self.label_14.setObjectName("label_14")
        self.lne_read = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_read.setEnabled(True)
        self.lne_read.setGeometry(QtCore.QRect(60, 360, 221, 91))
        self.lne_read.setObjectName("lne_read")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 340, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, 140, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(790, 290, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(730, 320, 170, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.laser_version_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.laser_version_button.setObjectName("laser_version_button")
        self.verticalLayout_6.addWidget(self.laser_version_button)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.laser_power_on_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.laser_power_on_button.setObjectName("laser_power_on_button")
        self.horizontalLayout_2.addWidget(self.laser_power_on_button)
        self.laser_power_off_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.laser_power_off_button.setObjectName("laser_power_off_button")
        self.horizontalLayout_2.addWidget(self.laser_power_off_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(90, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.laser_motor_position_slider = QtWidgets.QSlider(self.centralwidget)
        self.laser_motor_position_slider.setGeometry(QtCore.QRect(730, 430, 160, 16))
        self.laser_motor_position_slider.setOrientation(QtCore.Qt.Horizontal)
        self.laser_motor_position_slider.setObjectName("laser_motor_position_slider")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(640, 430, 81, 16))
        self.label_16.setObjectName("label_16")
        self.laser_reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.laser_reset_button.setGeometry(QtCore.QRect(770, 500, 80, 23))
        self.laser_reset_button.setObjectName("laser_reset_button")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(730, 190, 168, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.relay_on_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.relay_on_button.setObjectName("relay_on_button")
        self.horizontalLayout_3.addWidget(self.relay_on_button)
        self.relay_off_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.relay_off_button.setObjectName("relay_off_button")
        self.horizontalLayout_3.addWidget(self.relay_off_button)
        self.ptz_speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.ptz_speed_slider.setGeometry(QtCore.QRect(450, 180, 160, 16))
        self.ptz_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ptz_speed_slider.setObjectName("ptz_speed_slider")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(380, 180, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.laser_beam_angle_slider = QtWidgets.QSlider(self.centralwidget)
        self.laser_beam_angle_slider.setGeometry(QtCore.QRect(730, 460, 160, 16))
        self.laser_beam_angle_slider.setOrientation(QtCore.Qt.Horizontal)
        self.laser_beam_angle_slider.setObjectName("laser_beam_angle_slider")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(640, 460, 81, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(640, 480, 81, 16))
        self.label_19.setObjectName("label_19")
        self.laser_power_slider = QtWidgets.QSlider(self.centralwidget)
        self.laser_power_slider.setGeometry(QtCore.QRect(730, 480, 160, 16))
        self.laser_power_slider.setOrientation(QtCore.Qt.Horizontal)
        self.laser_power_slider.setObjectName("laser_power_slider")
        self.led_max_button = QtWidgets.QPushButton(self.centralwidget)
        self.led_max_button.setGeometry(QtCore.QRect(740, 400, 80, 23))
        self.led_max_button.setObjectName("led_max_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.left_button.setText(_translate("MainWindow", "Left"))
        self.up_button.setText(_translate("MainWindow", "Up"))
        self.right_button.setText(_translate("MainWindow", "Right"))
        self.down_button.setText(_translate("MainWindow", "Down"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Pelco Human Tracking System"))
        self.label_2.setText(_translate("MainWindow", "created by Microver Electronics"))
        self.test_button.setText(_translate("MainWindow", "PTZ Send Command"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.lineEdit.setText(_translate("MainWindow", "FF"))
        self.label_13.setText(_translate("MainWindow", "2"))
        self.byte2_lineEdit.setText(_translate("MainWindow", "01"))
        self.label_12.setText(_translate("MainWindow", "3"))
        self.byte3_lineEdit.setText(_translate("MainWindow", "FF"))
        self.label_11.setText(_translate("MainWindow", "4"))
        self.byte4_lineEdit.setText(_translate("MainWindow", "FF"))
        self.label_9.setText(_translate("MainWindow", "5"))
        self.byte5_lineEdit.setText(_translate("MainWindow", "FF"))
        self.label_8.setText(_translate("MainWindow", "6"))
        self.byte6_lineEdit.setText(_translate("MainWindow", "FF"))
        self.label_6.setText(_translate("MainWindow", "Sum"))
        self.bytesum_lineEdit.setText(_translate("MainWindow", "FF"))
        self.label_14.setText(_translate("MainWindow", "Byte"))
        self.label_3.setText(_translate("MainWindow", "RS485 Responses"))
        self.label_4.setText(_translate("MainWindow", "Custom Relay"))
        self.label_7.setText(_translate("MainWindow", "Laser"))
        self.laser_version_button.setText(_translate("MainWindow", "Version"))
        self.laser_power_on_button.setText(_translate("MainWindow", "Power On"))
        self.laser_power_off_button.setText(_translate("MainWindow", "Power Off"))
        self.label_10.setText(_translate("MainWindow", "PTZ Manuel Control"))
        self.label_15.setText(_translate("MainWindow", "PTZ Custom Command"))
        self.label_16.setText(_translate("MainWindow", "Motor Position"))
        self.laser_reset_button.setText(_translate("MainWindow", "Reset"))
        self.relay_on_button.setText(_translate("MainWindow", "Relay On"))
        self.relay_off_button.setText(_translate("MainWindow", "Relay Off"))
        self.label_17.setText(_translate("MainWindow", "PTZ Speed"))
        self.label_18.setText(_translate("MainWindow", "Beam Angle"))
        self.label_19.setText(_translate("MainWindow", "Laser Power"))
        self.led_max_button.setText(_translate("MainWindow", "Led Max"))
