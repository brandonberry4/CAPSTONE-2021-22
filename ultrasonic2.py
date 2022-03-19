import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 33
#TRIG2 = 23
ECHO1 = 31
#ECHO2 = 29

print ("Setup")
GPIO.setup(TRIG, GPIO.OUT)
#GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
#GPIO.setup(ECHO2, GPIO.IN)
GPIO.output(TRIG, False)
#GPIO.output(TRIG2, False)

def distance1():
    print("In dist1")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    print("Checking distance")
    
    while GPIO.input(ECHO1) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO1) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance
    
    print("out dist1")

# def distance2():
#     print("In dist2")
#     GPIO.output(TRIG, True)
#     time.sleep(0.00001)
#     GPIO.output(TRIG, False)
# 
#     while GPIO.input(ECHO2) == 0:
#         pulse_start = time.time()
#     while GPIO.input(ECHO2) == 1:
#         pulse_end = time.time()
#         
#     pulse_duration = pulse_end - pulse_start
#     distance = pulse_duration * 17150
#     distance = round(distance, 2)
    
    return distance
    
if __name__ == '__main__':
    try:
        while True:
            dist1 = distance1()
#             dist2 = distance2()
            print ("Measured Distance 1 = %.1f cm" % dist1)
#             print ("Measured Distance 2 = %.1f cm" % dist2)
            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()