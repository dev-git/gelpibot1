##############################################
# File Name: module6.py
# Version: 1.0
# Team No.: 20
# Team Name:
# Date: 11 Nov 15
##############################################

import RPi.GPIO as GPIO
import time

print 'Programming the PiBot...'

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

print 'forward'
GPIO.output(11, True)
GPIO.output(13, True)
time.sleep(1)
GPIO.output(11, False)
GPIO.output(13, False)
   
print 'back'
GPIO.output(7, True)
GPIO.output(15, True)
time.sleep(interval)
GPIO.output(7, False)
GPIO.output(15, False)

print 'left'
GPIO.output(13, True)
time.sleep(interval)
GPIO.output(13, False)
      
print 'right'
GPIO.output(11, True)
time.sleep(interval)
GPIO.output(11, False)

GPIO.cleanup()
   
print "\nPiBot is going offline..."
