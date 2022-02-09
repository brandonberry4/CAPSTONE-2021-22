import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
import time

GPIO.setup(36, GPIO.IN) #GPIO 36 right IR
GPIO.setup(32, GPIO.IN) #GPIO 32 left IR

while True:
    if (GPIO.input(32) == False and GPIO.input(36) == False): #both see black
         print("On track")
         time.sleep(0.5)
    elif (GPIO.input(32) == False and GPIO.input(36) == True): #right sees white
         print("Off track, turning right")
         time.sleep(0.5)
    elif (GPIO.input(32) == True and GPIO.input(36) == False): #left sees white
         print("Off track, turning left")
         time.sleep(0.5)
    elif (GPIO.input(32) == True and GPIO.input(36) == False): #right sees white
         print("Off track, turning right")
         time.sleep(0.5)
    elif (GPIO.input(32) == True and GPIO.input(36) == True): #both see white
         print("End of track stop")
         time.sleep(0.5)

















#     if (GPIO.input(32)) == False:
#         print("On track")
#         time.sleep(1)
#     elif (GPIO.input(32)) == True:
#         print("Off track")
#         time.sleep(1)