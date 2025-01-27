##############################################
# File Name: module3.py
# Version: 1.1
# Team No.: 1
# Team Name:
# Date: 20 Oct 23
##############################################

import RPi.GPIO as GPIO
import time
import sys, tty, termios

print('\nHi, I am PiBot, your very own learning robot...\n')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

ledOnTime = 10

# Turn on LED
print('Turn the LED on')
GPIO.output(7, True)
time.sleep(ledOnTime)
print('Turn the LED off')
GPIO.output(7, False)

GPIO.cleanup()
   
print("\nEnd of program")
