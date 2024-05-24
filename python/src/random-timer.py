# Imports go at the top

import random

import music
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

    hourglass_progress_2: Image = Image(
        "99999:"
        "09990:"
        "00900:"
        "09690:"
        "99999:"
    )  # fmt: off

    hourglass_progress_3: Image = Image(
        "99999:"
        "09990:"
        "00900:"
        "09090:"
        "99999:"
    )  # fmt: off


class RandomTimer:
    """Random Timer experiment"""

    def __init__(self) -> None:
        self.images: MyImages = MyImages()
        self.lower_bound: int = 10
        self.upper_bound: int = 90
        self.duration: int = 0

    def run(self) -> None:
        """Run the timer."""

        self.duration: int = random.randint(self.lower_bound, self.upper_bound)

        display.show(self.images.hourglass_start)
        sleep(1_000)

        print("INFO: starting " + str(self.duration) + " second timer")

        offset: int = 0

        for i in range(self.duration, 0, -1):
            if i < self.duration // 2:
                offset = 2

            display.show(getattr(self.images, "hourglass_progress_" + str(offset + (i % 2))))
            sleep(1_000)

        print("INFO: timer has completed")
        display.show(self.images.hourglass_end)

        music.play(music.BA_DING)


print()
print("Random Timer")
print()


app: RandomTimer = RandomTimer()

# Code in a 'while True:' loop repeats forever
while True:
    app.run()

    sleep(5_000)
