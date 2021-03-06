import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import time
import os
import Infrared
import Ultrasonic
import Motor
#from object_tracking import object_tracking

count = 0
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("Waiting for press")
try:
    while (1):
        inputValue = GPIO.input(8)
        if(inputValue == False):
            print("Button pressed")
            count = count + 1
            if count == 1:
                print("Robot running")
                time.sleep(5)
                Motor.StartMoving() #Starts driving forward from begining
                Motor.fullStop()
                time.sleep(2)
                Infrared.trackLine()
                Motor.goBackward()
                time.sleep(2)
                Infrared.trackLineRev()
                time.sleep(1)
                Motor.goHome()
            elif count == 2:
                print("Reset")
                Motor.setup()
                count = 0
except KeyboardInterrupt:
    quit()
