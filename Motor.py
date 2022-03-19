import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
# Pins for Motor Driver Inputs
# Left side
Motor1 = 11 #input
Motor2 = 13 #input
Motor3 = 15 #enable

GPIO.setup(Motor3,GPIO.OUT)
p1 = GPIO.PWM(15, 100)

# Right side
Motor4 = 16 #input
Motor5 = 18 #input
Motor6 = 22 #enable

GPIO.setup(Motor6,GPIO.OUT)
p2 = GPIO.PWM(22, 100)

p1.start(0)
p2.start(0)


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
    print("Wait")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
    
def StartMoving():
    print("Moving forward")
    p1.ChangeDutyCycle(70)
    p2.ChangeDutyCycle(70)
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Forward")
    sleep(2.5)
    
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    print("Pivot Right")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(1.5)
    
def TurnAround():
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    print("Turn Around")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(3)
    
    
def goForward():
    p1.ChangeDutyCycle(90)
    p2.ChangeDutyCycle(90)
    print("going forward")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Forward")
    
def goBackward():
    p1.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    print("going backward")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(5)
    print ("Reverse")
    
def fullStop():
    print("Full stop")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
    print("Stop")

def stopLeft():
    print("Stopping left")
    #GPIO.output(Motor3,GPIO.LOW)
    
def stopRight():
    print("Stopping right")
    #GPIO.output(Motor6,GPIO.LOW)

# def loop():
# # Going forwards
#     GPIO.output(Motor1,GPIO.HIGH)
#     GPIO.output(Motor2,GPIO.LOW)
#     GPIO.output(Motor3,GPIO.HIGH)#
#     GPIO.output(Motor4,GPIO.HIGH)
#     GPIO.output(Motor5,GPIO.LOW)
#     GPIO.output(Motor6,GPIO.HIGH)
#     print ("Forward")
#     sleep(5)
# # Going backwards
#     GPIO.output(Motor1,GPIO.LOW)
#     GPIO.output(Motor2,GPIO.HIGH)
#     GPIO.output(Motor3,GPIO.HIGH)
#     GPIO.output(Motor4,GPIO.LOW)
#     GPIO.output(Motor5,GPIO.HIGH)
#     GPIO.output(Motor6,GPIO.HIGH)
#     print ("Reverse")
#     sleep(5) 
# # Stop
#     GPIO.output(Motor3,GPIO.LOW)
#     GPIO.output(Motor6,GPIO.LOW)
#     print("Stop")

def turnLeft():
    p2.ChangeDutyCycle(70)
    print("Turning left")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    
def turnRight():
    p1.ChangeDutyCycle(70)
    print("Turning right")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
    
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__': # Program start from here
    # dist = ultrasonic.distance()
    setup()
    print ("Working")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()