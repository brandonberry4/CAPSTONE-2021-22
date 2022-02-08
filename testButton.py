from gpiozero import Button
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
import time

count = 0
#button = Button(25) #pin 11

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        time.sleep(0.5)
        count = count + 1
    if count == 1:
        print("Robot running")
    if count == 3:
        print("Stopping")
        quit() #kill switch
    
    #button.wait_for_press()
    #count = count + 1
    #time.sleep(0.5) # wait in between button press
    #print(count)
    
    #if button.wait_for_press() == True:
    #    subprocess.call(['python', 'startAll.py']) #runs startAll
    #elif count == 3:
    #    quit() #kill switch