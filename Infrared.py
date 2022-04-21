import time
import gpiozero
import Motor
import Ultrasonic
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


line_sensorRight = gpiozero.DigitalInputDevice(19)
line_sensorLeft = gpiozero.DigitalInputDevice(26)
Motor.setup()

GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
count = 0
inputValue = GPIO.input(8)

def trackLine():
    while True:
        if line_sensorRight.is_active == True and line_sensorLeft.is_active == True:
            print("On track")
            Motor.goForward()
            time.sleep(0.5)
        elif line_sensorRight.is_active == True and line_sensorLeft.is_active == False: #turn left
            print("Turn left")
            Motor.turnLeft()
            time.sleep(0.5)
        elif line_sensorRight.is_active == False and line_sensorLeft.is_active == True: #turn right
            print("Turn right")
            Motor.turnRight()
            time.sleep(0.5)
        else:
            print("Stop")
            Motor.fullStop()
            break
        
def trackLineRev():
    while Ultrasonic.distance() > 35:
        if line_sensorRight.is_active == True and line_sensorLeft.is_active == True:
            print("On track")
            Motor.goBackward()
            time.sleep(0.5)
        elif line_sensorRight.is_active == False and line_sensorLeft.is_active == True: #turn left
            print("Turn left")
            Motor.turnRightRev()
            time.sleep(0.5)
        elif line_sensorRight.is_active == True and line_sensorLeft.is_active == False: #turn right
            print("Turn right")
            Motor.turnLeftRev()
            time.sleep(0.5)
        elif Ultrasonic.distance() < 35:
            print("Stop")
            Motor.fullStop()
            quit()

