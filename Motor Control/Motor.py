import RPi.GPIO as GPIO
from /home/pi/Desktop/Robot Code/UltrasonicSensor
from time import sleep
GPIO.setmode(GPIO.BOARD)
# Pins for Motor Driver Inputs
# Left side
Motor1 = 16 #input
Motor2 = 18 #input
Motor3 = 22 #enable
# Right side
Motor4 = 11 #input
Motor5 = 13 #input
Motor6 = 15 #enable
GPIO.setwarnings(False)
def setup():
    GPIO.setup(Motor1,GPIO.OUT) # Left side as Outputs
    GPIO.setup(Motor2,GPIO.OUT)
    GPIO.setup(Motor3,GPIO.OUT)
    GPIO.setup(Motor4,GPIO.OUT) # Right side as Outputs
    GPIO.setup(Motor5,GPIO.OUT)
    GPIO.setup(Motor6,GPIO.OUT)
    print ("Setup")
    sleep(1)
    print("Waiting 3")
    sleep(1)
    print("Waiting 2")
    sleep(1)
    print("Waiting 1")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
def loop():
# Going forwards
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Forward")
    sleep(5)
# Going backwards
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Reverse")
    sleep(5) 
# Stop
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
    print("Stop")
    
    
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__': # Program start from here
    setup()
    print ("Working")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()