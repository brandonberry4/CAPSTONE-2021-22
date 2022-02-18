#import RPi.GPIO as GPIO
# GPIO.setwarnings(False)
# GPIO.setmode (GPIO.BCM)
import time
import gpiozero

# GPIO.setup(35, GPIO.IN) #GPIO 35 right IR
# GPIO.setup(37, GPIO.IN) #GPIO 37 left IR

# while True:
#     if (GPIO.input(35) == False and GPIO.input(37) == False): #both see black
#         print("On track")
#         time.sleep(0.5)
#         continue
#     elif (GPIO.input(37) == False and GPIO.input(35) == True): #turn right
#         print("Off track, turning right")
#         time.sleep(0.5)
#         continue
#     elif (GPIO.input(37) == True and GPIO.input(35) == False): #turn left
#         print("Off track, turning left")
#         time.sleep(0.5)
#         continue
#     else: # stop
#         print("End of track, stopping")
#         time.sleep(0.5)

line_sensorRight = gpiozero.DigitalInputDevice(19)
line_sensorLeft = gpiozero.DigitalInputDevice(26)

while True:
    if line_sensorRight.is_active == True and line_sensorLeft.is_active == True:
        print("On track")
        time.sleep(0.5)
    elif line_sensorRight.is_active == True and line_sensorLeft.is_active == False: #turn left
        print("Turn left")
        time.sleep(0.5)
    elif line_sensorRight.is_active == False and line_sensorLeft.is_active == True: #turn right
        print("Turn right")
        time.sleep(0.5)
    else:
        print("Stop")
        time.sleep(0.5)
        break

















#     if (GPIO.input(32)) == False:
#         print("On track")
#         time.sleep(1)
#     elif (GPIO.input(32)) == True:
#         print("Off track")
#         time.sleep(1)