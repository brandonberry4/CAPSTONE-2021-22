import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Pins for Motor Driver Inputs
# Left side
Motor1 = 17 #input 11
Motor2 = 27 #input 13
Motor3 = 22 #enable 15

GPIO.setup(Motor3,GPIO.OUT)
p1 = GPIO.PWM(22, 100)

# Right side
Motor4 = 23 #input 16
Motor5 = 24 #input 18
Motor6 = 25 #enable 22

GPIO.setup(Motor6,GPIO.OUT)
p2 = GPIO.PWM(25, 100)

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
    print ("Motor Setup")
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
    p1.ChangeDutyCycle(30)
    p2.ChangeDutyCycle(30)
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Forward")
    sleep(1.65)
    
    p1.ChangeDutyCycle(56)
    p2.ChangeDutyCycle(56)
    print("Pivot Right")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(1.35)
    
    
def TurnAround():
    #p1.ChangeDutyCycle(20)
    #p2.ChangeDutyCycle(20)
    #sleep(0.3)
    p1.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    print("Turn Around")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(2)
    
    
def goForward():
    #p1.ChangeDutyCycle(10)
    #p2.ChangeDutyCycle(10)
    #sleep(0.3)
    p1.ChangeDutyCycle(34)
    p2.ChangeDutyCycle(34)
    print("going forward")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Forward")
    
def goBackward():
    #p1.ChangeDutyCycle(10)
    #p2.ChangeDutyCycle(10)
    #sleep(0.3)
    p1.ChangeDutyCycle(20)
    p2.ChangeDutyCycle(20)
    print("going backward")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(1)
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

def turnLeft():
    p2.ChangeDutyCycle(50)
    print("Turning left")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    
def turnRight():
    p1.ChangeDutyCycle(50)
    print("Turning right")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
    
def pushMarsh():
    p1.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)
    print("Pushing Marshmallow")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)
    sleep(0.7)
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(0.8)
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(0.8)
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(0.7)
    
def goHome():
    
    p1.ChangeDutyCycle(56)
    p2.ChangeDutyCycle(56)
    print("Pivot Right")
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    sleep(1.72)

    p1.ChangeDutyCycle(35)
    p2.ChangeDutyCycle(35)
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    print ("Forward")
    sleep(1.4)
    quit()
    
def turnRightRev():
    p2.ChangeDutyCycle(30)
    print("Turning right backwards")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.LOW)
    
def turnLeftRev():
    p1.ChangeDutyCycle(30)
    print("Turning left backwards")
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.LOW)    
        
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__': # Program start from here
    # dist = ultrasonic.distance()
    setup()
    print ("Working")
    try:
        while True:
            #turnRight()
            #turnLeft()
            turnLeftRev()
            #turnRightRev()
    except KeyboardInterrupt:
        GPIO.cleanup()