import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 40
ECHO = 38
maxTime = 0.02
total = 0
count = 0
distance = 0
avg = 0
dist = []
distList = []
scan = False

print ("US Setup")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

def distance():
    hist = []
    
    starttime = time.time()
    for i in range(10):
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        pulse_start = time.time()
        timeout = pulse_start + maxTime
        while GPIO.input(ECHO) == 0 and pulse_start < timeout:
            pulse_start = time.time()
        pulse_end = time.time()
        timeout = pulse_end + maxTime
        while GPIO.input(ECHO) == 1 and pulse_start < timeout:
            pulse_end = time.time()
        

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        hist.append(distance)
        
    validcount = 0
    total = 0
    print(hist)
    for i in hist:
        if i < 130:
            validcount += 1
            total += 1
        if validcount > 1:
            avg_dist = round(total/validcount, 2)
            if avg_dist <= 50:
                return ([avg_dist, True, avg_dist, avg_dist])
            else:
                return ([avg_dist, False, avg_dist, avg_dist]) 
        avg_temp = 0
        for i in range(10):
            avg_temp += hist[i]
        return avg_temp/10
        
    
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Average Distance = %.1f cm" % dist)
            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
