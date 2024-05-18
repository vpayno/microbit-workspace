# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    for image in dir(Image):
        if image.isupper():
            print("image: " + image)
            display.show(getattr(Image, image))
            sleep(5_000)
