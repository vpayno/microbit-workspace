# Imports go at the top
import speech
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    print("Hello world!")

    # scrolls the letters on the dot display
    display.scroll("Hello world!")

    # prints one letter at a time, no sliding
    display.show("Hello world!")

    for vol in (0, 63, 127, 191, 255):
        print("INFO: volume set to " + str(vol))
        set_volume(255)
        # it's just noise
        speech.say("Hello world!")

    # not the creepy giggle I was hopeing for
    print("INFO: Gigggle")
    audio.play(Sound.GIGGLE)
    sleep(1_000)
    print("INFO: HELLO")
    # closer to the sound "hello"
    audio.play(Sound.HELLO)
    sleep(1_000)
