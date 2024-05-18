# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    sound_level: int = microphone.sound_level()
    print("INFO: sound level (0..255): " + str(sound_level))
    display.scroll(sound_level)
