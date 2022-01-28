import RPi.GPIO as GPIO
import time
import subprocess
from gpiozero import Button

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



count = 0
if GPIO.input(11) == GPIO.LOW:
        print("Button Ready")

while True:   
    if GPIO.input(11) == GPIO.HIGH:
        print("Button was pushed")
        time.sleep(2)
        

    


#while True:
#    input_state = GPIO.input(11)
#    if input_state == False:
#        subprocess.call(['python', 'startAll.py']) #runs startAll