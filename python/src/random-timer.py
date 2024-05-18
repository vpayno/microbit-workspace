# Imports go at the top
import random

from microbit import *


class MyImages:
    hourglass_start: Image = Image(
        "99999:"
        "09990:"
        "00900:"
        "09090:"
        "90009:"
    )  # fmt: off

    hourglass_end: Image = Image(
        "90009:"
        "09090:"
        "00900:"
        "09990:"
        "99999:"
    )  # fmt: off

    hourglass_progress_0: Image = Image(
        "99999:"
        "09990:"
        "00900:"
        "09690:"
        "90009:"
    )  # fmt: off

    hourglass_progress_1: Image = Image(
        "99999:"
        "09990:"
        "00900:"
        "09090:"
        "90609:"
    )  # fmt: off


myimages = MyImages()

print("INFO: Random Hourglass Timer")

# Code in a 'while True:' loop repeats forever
while True:
    seconds: int = random.randint(10, 90)
    display.show(myimages.hourglass_start)
    sleep(1_000)

    print("INFO: starting " + str(seconds) + " second timer")
    for i in range(0, seconds):
        display.show(getattr(myimages, "hourglass_progress_" + str(i % 2)))
        sleep(1_000)

    print("INFO: timer has completed")
    display.show(myimages.hourglass_end)
    sleep(1_000)
