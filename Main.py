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
                time.sleep(2)
                Motor.goForward()
                print("Robot running")
#            #Ultrasonic.distance()
#            #Motor.StartMoving()
#            #Infrared.trackLine()
#            #if Ultrasonic.distance() < 30:
#            #    Motor.StartMoving() #Starts driving forward from begining
#            #    Infrared.trackLine()  #Turns on line tracking to move down course
#            #    time.sleep(1)
#            #Motor.pushMarsh()
#            #Infrared.trackLine()
#            Motor.goBackward()  #Once at end of course back up to get more room
#            #Motor.TurnAround()  #Turns around
#            #Infrared.trackLine()  #Line track back to beginning
#            #if Ultrasonic.distance1() < 20:
#            #    Infrared.trackLineRev()
#            #Motor.goHome()
            elif count == 3:
                print("Reset")
                Motor.setup()
                count = 0
                GPIO.cleanup()
        
        
