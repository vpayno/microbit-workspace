# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    for sound in dir(Sound):
      if sound.isupper():
        print("sound: " + sound)
        audio.play(getattr(Sound, sound))
        sleep(1000)
