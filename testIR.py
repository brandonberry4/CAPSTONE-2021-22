import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
import time

GPIO.setup(35, GPIO.IN) #GPIO 35 right IR
GPIO.setup(37, GPIO.IN) #GPIO 37 left IR


if (GPIO.input(35) == False and GPIO.input(37) == False): #both see black
    print("On track")
    time.sleep(0.5)
elif (GPIO.input(37) == False and GPIO.input(35) == True): #turn right
    print("Off track, turning right")
    time.sleep(0.5)
elif (GPIO.input(37) == True and GPIO.input(35) == False): #turn left
    print("Off track, turning left")
    time.sleep(0.5)
else: #stop
    print("End of track, stopping")




















#     if (GPIO.input(32)) == False:
#         print("On track")
#         time.sleep(1)
#     elif (GPIO.input(32)) == True:
#         print("Off track")
#         time.sleep(1)