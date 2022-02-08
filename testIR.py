import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
import time

GPIO.setup(0, GPIO.IN) #GPIO 0 right IR
GPIO.setup(2, GPIO.IN) #GPIO 2 left IR

while True:
    if (GPIO.input(0) == True and GPIO.input(2) == True): #both see white
        print("Checking")
        print("On track")
        time.sleep(1)

