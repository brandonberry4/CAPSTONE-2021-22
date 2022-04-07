from gpiozero import Button
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
import time
import os
import testIR
import ultrasonic2
import ultrasonic
import Motor

count = 0
button = Button(27, None, True) #pin 36 GPIO 27


GPIO.setup(36, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    if GPIO.input(36) == GPIO.HIGH:
        time.sleep(0.3)
        count = count + 1   
    if count == 1:
        time.sleep(3)
        print("Robot running")
        if ultrasonic2.distance1() < 120:
            Motor.StartMoving() #Starts driving forward from begining
            testIR.trackLine()  #Turns on line tracking to move down course
            time.sleep(1)
        Motor.pushMarsh()
        testIR.trackLine()
        Motor.goBackward()  #Once at end of course back up to get more room
        Motor.TurnAround()  #Turns around
        testIR.trackLine()  #Line track back to beginning
        if ultrasonic2.distance1() < 20:
            testIR.trackLineRev()
        Motor.goHome()
    elif count == 2:
        print("Stopping")
        quit()
        #os.system("sudo shutdown -h now")
        
        
