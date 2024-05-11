# Imports go at the top
import random

from microbit import *

DEGREES_N: int = 0
DEGREES_NE: int = 45
DEGREES_E: int = 90
DEGREES_SE: int = 135
DEGREES_S: int = 180
DEGREES_SW: int = 225
DEGREES_W: int = 270
DEGREES_NW: int = 315
DEGREES_N_ALT: int = 360

heading: int = 0

print("INFO: Using the RNG to turn the arrow")


def turn_clockwise(heading: int) -> int:
    if heading >= DEGREES_N_ALT:
        heading = 0
    else:
        heading += 5
    return heading


def turn_counter_clockwise(heading: int) -> int:
    if heading <= DEGREES_N:
        heading = 359
    else:
        heading -= 5
    return heading


# Code in a 'while True:' loop repeats forever
while True:
    print("INFO: heading: " + str(heading) + "°")

    if (heading >= DEGREES_N and heading <= (DEGREES_N + 22)) or (
        heading < DEGREES_N_ALT and heading >= (DEGREES_N_ALT - 22)
    ):
        print("INFO: NORTH is between 337°-360°, 0°-22°")
        display.show(Image.ARROW_N)

    elif (heading <= DEGREES_NE and heading >= (DEGREES_NE - 23)) or (
        heading >= DEGREES_NE and heading <= (DEGREES_NE + 23)
    ):
        print("INFO: NORTH EAST is between 23°-45°, 45°-67°")
        display.show(Image.ARROW_NE)

    elif (heading <= DEGREES_E and heading >= (DEGREES_E - 22)) or (
        heading >= DEGREES_E and heading <= (DEGREES_E + 22)
    ):
        print("INFO: EAST is between 23°-45°, 45°-67°")
        display.show(Image.ARROW_E)

    elif (heading <= DEGREES_SE and heading >= (DEGREES_SE - 23)) or (
        heading >= DEGREES_SE and heading <= (DEGREES_SE + 23)
    ):
        print("INFO: SOUTH EAST is between 23°-45°, 45°-67°")
        display.show(Image.ARROW_SE)

    elif (heading <= DEGREES_S and heading >= (DEGREES_S - 22)) or (
        heading >= DEGREES_S and heading <= (DEGREES_S + 22)
    ):
        print("INFO: SOUTH is between 203°-180°, 180°-158°")
        display.show(Image.ARROW_S)

    elif (heading >= DEGREES_SW and heading <= (DEGREES_SW + 23)) or (
        heading <= DEGREES_SW and heading >= (DEGREES_SW - 23)
    ):
        print("INFO: SOUTH WEST is between 292°-270°, 270°-248°")
        display.show(Image.ARROW_SW)

    elif (heading >= DEGREES_W and heading <= (DEGREES_W + 22)) or (
        heading <= DEGREES_W and heading >= (DEGREES_W - 22)
    ):
        print("INFO: WEST is between 292°-270°, 270°-248°")
        display.show(Image.ARROW_W)

    elif (heading >= DEGREES_NW and heading <= (DEGREES_NW + 23)) or (
        heading <= DEGREES_NW and heading >= (DEGREES_NW - 23)
    ):
        print("INFO: NORTH WEST is between 292°-270°, 270°-248°")
        display.show(Image.ARROW_NW)

    sleep(2000)

    heading = random.randint(DEGREES_N, DEGREES_N_ALT)
