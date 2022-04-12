import time
import gpiozero
import Motor


line_sensorRight = gpiozero.DigitalInputDevice(19)
line_sensorLeft = gpiozero.DigitalInputDevice(26)
Motor.setup()

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
    while True:
        if line_sensorRight.is_active == True and line_sensorLeft.is_active == True:
            print("On track")
            Motor.goBackward()
            time.sleep(0.5)
        elif line_sensorRight.is_active == False and line_sensorLeft.is_active == True: #turn left
            print("Turn left")
            Motor.turnLeft()
            time.sleep(0.5)
        elif line_sensorRight.is_active == True and line_sensorLeft.is_active == False: #turn right
            print("Turn right")
            Motor.turnRight()
            time.sleep(0.5)
        else:
            print("Stop")
            Motor.fullStop()
            break
        
