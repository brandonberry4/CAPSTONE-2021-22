from gpiozero import Button
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
import time
import os
import testIR

count = 0
button = Button(27, None, True) #pin 36 GPIO 27

#button.wait_for_press()
#print("Button pressed")

GPIO.setup(36, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    if GPIO.input(36) == GPIO.HIGH:
        time.sleep(0.3)
        count = count + 1   
    if count == 1:
        print("Robot running")
        testIR.trackLine()
        break
    elif count == 2:
        print("Stopping")
        quit()
        #os.system("sudo shutdown -h now") 



# while True: # Run forever    
#     button.wait_for_press()
#     time.sleep(0.5) # wait in between button press
#     
#     if button.is_pressed():
#         testIR.trackLine()
#     elif button.is_pressed():
#         quit() #kill switch