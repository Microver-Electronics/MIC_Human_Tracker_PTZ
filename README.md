# Pelco PTZ Human Tracker

This is a project that performs body detection and tracking human bodies with Pelco PTZ via rs485 communication.

## Requirements

- Intel OpenVino Dev Kit
- Opencv
- PyQt5
- MobileNetSSD_deploy.prototxt
- MobileNetSSD_deploy.caffemodel

## Installation and Run

- sh init.sh
- sudo python3 gui.py
- sudo python3 body_tracker.py

## Dev Proccess

- pyuic5 gui\mainwindow.ui -o gui\mainwindow.py

## Comm

- RS485

## Specs

- Face Tracking
- Graphical User Interface for manuel control Pelco PTZ
