# Imports go at the top
from microbit import *

# type annocations seem to work
counter: int = 0

# Code in a 'while True:' loop repeats forever
while True:
    counter += 1

    # touch the logo to make the microbit happy (don't call HR)
    if pin_logo.is_touched():
        counter = 0
        print("INFO: happy")
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
        sleep(5000)
    else:
        if counter <= 10:
            print("INFO: sad")
            display.show(Image.SAD)
            audio.play(Sound.SAD)
            sleep(1000)
        else:
            print("INFO: angry")
            display.show(Image.ANGRY)
            # this sounds more like a bird call
            audio.play(Sound.YAWN)
            sleep(1000)

