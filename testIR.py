import time
import gpiozero


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