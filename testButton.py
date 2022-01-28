from gpiozero import Button
import time

count = 0
button = Button(11) #pin 11

while True:
    button.wait_for_press()
    count = count + 1
    time.sleep(0.5) # wait in between button press
    
    if button.wait_for_press() == True:
        subprocess.call(['python', 'startAll.py']) #runs startAll
    else if count == 3:
        quit() #kill switch