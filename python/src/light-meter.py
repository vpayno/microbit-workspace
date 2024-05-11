# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    # not very sensitive, well lit room registers at 0
    # using cell phone flash light near it get at least 100 score
    light_level: int = display.read_light_level()
    print("INFO: light level is " + str(light_level))
    display.scroll(light_level)
