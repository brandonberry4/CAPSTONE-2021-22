#Libraries
import RPi.GPIO as GPIO
import Motor
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 7
GPIO_ECHO = 11
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    print("DISTANCE STARTS")
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    #GPIO.setup(Motor.Motor1,GPIO.OUT) # Left side as Outputs
    #GPIO.setup(Motor.Motor2,GPIO.OUT)
    #GPIO.setup(Motor.Motor3,GPIO.OUT)
    #GPIO.setup(Motor.Motor4,GPIO.OUT) # Right side as Outputs
    #GPIO.setup(Motor.Motor5,GPIO.OUT)
    #GPIO.setup(Motor.Motor6,GPIO.OUT)
    try:
        while True:
            print("Loop")
            dist = distance()
            #if(dist >50):
                #Motor.goForward()
            #    time.sleep(5.0)
            #else:
                #Motor.goBackward()
            #    time.sleep(5.0)
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()