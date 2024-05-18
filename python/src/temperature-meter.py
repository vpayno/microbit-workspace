# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # not very sensitive, well lit room registers at 0
    # using cell phone flash light near it get at least 100 score
    temp_c: int = temperature()
    temp_f: int = round(temp_c * (9 / 5)) + 32

    print("INFO: the ambient temperature is " + str(temp_c) + "°C")
    print("INFO: the ambient temperature is " + str(temp_f) + "°F")

    # using ° here results in '??'
    display.scroll(str(temp_c) + "C" + " | " + str(temp_f) + "F" + " | ")
