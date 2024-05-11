# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        print("INFO: user pressed button A")
        display.show(Image.ARROW_W)
        sleep(5000)
    elif button_b.was_pressed():
        print("INFO: user pressed button B")
        display.show(Image.ARROW_E)
        sleep(5000)
    else:
        print("INFO: waiting on input")
        display.show(Image.ALL_ARROWS)
