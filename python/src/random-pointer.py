# Imports go at the top
import random

import music
from microbit import *


class RandomPointer:
    """Basically it's a broken compass."""

    DEGREES_N: int = 0
    DEGREES_NE: int = 45
    DEGREES_E: int = 90
    DEGREES_SE: int = 135
    DEGREES_S: int = 180
    DEGREES_SW: int = 225
    DEGREES_W: int = 270
    DEGREES_NW: int = 315
    DEGREES_N_ALT: int = 360

    def __init__(self) -> None:
        self.heading: int = 0
        self.mute: bool = False

    def turn_clockwise(self) -> None:
        if self.heading >= self.DEGREES_N_ALT:
            self.heading = 0
        else:
            self.heading += 5

    def turn_counter_clockwise(self) -> None:
        if self.heading <= self.DEGREES_N:
            self.heading = 359
        else:
            self.heading -= 5

    def step(self) -> None:
        self.mute_control()

        self.heading = random.randint(self.DEGREES_N, self.DEGREES_N_ALT)

        self.draw_arrow()

        if self.mute:
            music.play(music.BA_DING)

    def draw_arrow(self) -> None:
        print("INFO: self.heading: " + str(self.heading) + "°")

        if (self.heading >= self.DEGREES_N and self.heading <= (self.DEGREES_N + 22)) or (
            self.heading < self.DEGREES_N_ALT and self.heading >= (self.DEGREES_N_ALT - 22)
        ):
            print("INFO: NORTH is between 337°-360°, 0°-22°")
            display.show(Image.ARROW_N)

        elif (self.heading <= self.DEGREES_NE and self.heading >= (self.DEGREES_NE - 23)) or (
            self.heading >= self.DEGREES_NE and self.heading <= (self.DEGREES_NE + 23)
        ):
            print("INFO: NORTH EAST is between 23°-45°, 45°-67°")
            display.show(Image.ARROW_NE)

        elif (self.heading <= self.DEGREES_E and self.heading >= (self.DEGREES_E - 22)) or (
            self.heading >= self.DEGREES_E and self.heading <= (self.DEGREES_E + 22)
        ):
            print("INFO: EAST is between 23°-45°, 45°-67°")
            display.show(Image.ARROW_E)

        elif (self.heading <= self.DEGREES_SE and self.heading >= (self.DEGREES_SE - 23)) or (
            self.heading >= self.DEGREES_SE and self.heading <= (self.DEGREES_SE + 23)
        ):
            print("INFO: SOUTH EAST is between 23°-45°, 45°-67°")
            display.show(Image.ARROW_SE)

        elif (self.heading <= self.DEGREES_S and self.heading >= (self.DEGREES_S - 22)) or (
            self.heading >= self.DEGREES_S and self.heading <= (self.DEGREES_S + 22)
        ):
            print("INFO: SOUTH is between 203°-180°, 180°-158°")
            display.show(Image.ARROW_S)

        elif (self.heading >= self.DEGREES_SW and self.heading <= (self.DEGREES_SW + 23)) or (
            self.heading <= self.DEGREES_SW and self.heading >= (self.DEGREES_SW - 23)
        ):
            print("INFO: SOUTH WEST is between 292°-270°, 270°-248°")
            display.show(Image.ARROW_SW)

        elif (self.heading >= self.DEGREES_W and self.heading <= (self.DEGREES_W + 22)) or (
            self.heading <= self.DEGREES_W and self.heading >= (self.DEGREES_W - 22)
        ):
            print("INFO: WEST is between 292°-270°, 270°-248°")
            display.show(Image.ARROW_W)

        elif (self.heading >= self.DEGREES_NW and self.heading <= (self.DEGREES_NW + 23)) or (
            self.heading <= self.DEGREES_NW and self.heading >= (self.DEGREES_NW - 23)
        ):
            print("INFO: NORTH WEST is between 292°-270°, 270°-248°")
            display.show(Image.ARROW_NW)

    def mute_control(self) -> None:
        """Toggles mute flag when either button is pressed."""

        if button_a.was_pressed() or button_b.was_pressed():
            print("INFO: button pressed, toggling mute")
            self.mute = not self.mute
            print("INFO: mute " + "enabled" if self.mute else "disabled")


print()
print("Random Pointer")
print()

print("INFO: Using the RNG to turn the arrow")

app: RandomPointer = RandomPointer()

# Code in a 'while True:' loop repeats forever
while True:
    app.step()

    sleep(5_000)
