#!/usr/bin/env python
#title           : pigopro_camera-test.py
#description     : 
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#notes           : http://www.raspberrypi.org/documentation/usage/camera/raspicam/README.md
#				   http://www.raspberrypi.org/documentation/usage/camera/python/README.md
#				   http://cya.nyc/2015/04/raspberry-pi-action-camera/
#				   http://www.raspberrypi-spy.co.uk/2014/11/how-to-create-a-raspberry-pi-video-capture-unit-part-1/
#
#python_version  : 2.7
#==============================================================================

# Import required Python libraries
import RPi.GPIO as GPIO
import time
import os

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_BUTTON = 17

# Set GPIO pins (input/output)
GPIO.setup(GPIO_BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_UP)


video_loc = "/home/pi/Documents/Videos"
video_dur = 30000 #in milliseconds (1000 milliceconds = 1 second)
DATE = time.strftime("%Y%m%d_%H%M%S")

print video_loc

try:  
 while True:
    if GPIO.input(switch_pin) == False:
        # take short video
		os.system ("raspivid -o " + video_loc + DATE + ".h264" -t video_dur) #sh command
		time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit