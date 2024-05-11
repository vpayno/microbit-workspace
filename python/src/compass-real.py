# Imports go at the top
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

print("If you don't see any output, please calibrate the compass.")


def draw_arrows(bearing: str) -> None:
    display.clear()

    north_arrow(bearing)
    south_arrow(bearing)
    west_arrow(bearing)
    east_arrow(bearing)


def north_arrow(bearing: str) -> None:
    # 0,0 -> top-left corner
    column: int = 0
    row: int = 0
    brightness: int = 9

    if bearing == "north":
        column = 2
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column, row + 1, brightness - 3)
        display.set_pixel(column, row + 2, brightness - 6)

    elif bearing == "north-east":
        column = 0
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column + 1, row + 1, brightness - 3)
        display.set_pixel(column + 2, row + 2, brightness - 6)

    elif bearing == "east":
        column = 0
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column + 1, row, brightness - 3)
        display.set_pixel(column + 2, row, brightness - 6)

    elif bearing == "south-east":
        column = 0
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column + 1, row - 1, brightness - 3)
        display.set_pixel(column + 2, row - 2, brightness - 6)

    elif bearing == "south":
        column = 2
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column, row - 1, brightness - 3)
        display.set_pixel(column, row - 2, brightness - 6)

    elif bearing == "south-west":
        column = 4
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column - 1, row - 1, brightness - 3)
        display.set_pixel(column - 2, row - 2, brightness - 6)

    elif bearing == "west":
        column = 4
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column - 1, row, brightness - 3)
        display.set_pixel(column - 2, row, brightness - 6)

    elif bearing == "north-west":
        column = 4
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)
        display.set_pixel(column - 1, row + 1, brightness - 3)
        display.set_pixel(column - 2, row + 2, brightness - 6)


def south_arrow(bearing: str) -> None:
    # 0,0 -> top-left corner
    column: int = 0
    row: int = 0
    brightness: int = 9 - 3

    if bearing == "north":
        column = 2
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "north-east":
        column = 4
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "east":
        column = 4
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south-east":
        column = 4
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south":
        column = 2
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south-west":
        column = 0
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "west":
        column = 0
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "north-west":
        column = 0
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)


def west_arrow(bearing: str) -> None:
    # 0,0 -> top-left corner
    column: int = 0
    row: int = 0
    brightness: int = 9 - 6

    if bearing == "north":
        column = 0
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "north-east":
        column = 0
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "east":
        column = 2
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south-east":
        column = 4
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south":
        column = 4
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south-west":
        column = 4
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "west":
        column = 2
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "north-west":
        column = 0
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)


def east_arrow(bearing: str) -> None:
    # 0,0 -> top-left corner
    column: int = 0
    row: int = 0
    brightness: int = 9 - 6

    if bearing == "north":
        column = 4
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "north-east":
        column = 4
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "east":
        column = 2
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south-east":
        column = 0
        row = 0
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south":
        column = 0
        row = 2
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "south-west":
        column = 0
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "west":
        column = 2
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)

    elif bearing == "north-west":
        column = 4
        row = 4
        # column (0..4), row (0..4), brightness (0..9)
        display.set_pixel(column, row, brightness)


# Code in a 'while True:' loop repeats forever
while True:
    # this call will make you play fill the screen/dots to calibrate
    # the compas - when it's ready it will display a smily face
    heading: int = compass.heading()
    print("INFO: heading: " + str(heading) + "°")

    if (heading >= DEGREES_N and heading <= (DEGREES_N + 22)) or (
        heading < DEGREES_N_ALT and heading >= (DEGREES_N_ALT - 22)
    ):
        print("INFO: NORTH is between 337°-360°, 0°-22°")
        draw_arrows("north")

    elif (heading <= DEGREES_NE and heading >= (DEGREES_NE - 23)) or (
        heading >= DEGREES_NE and heading <= (DEGREES_NE + 23)
    ):
        print("INFO: NORTH EAST is between 23°-45°, 45°-67°")
        draw_arrows("north-east")

    elif (heading <= DEGREES_E and heading >= (DEGREES_E - 22)) or (
        heading >= DEGREES_E and heading <= (DEGREES_E + 22)
    ):
        print("INFO: EAST is between 23°-45°, 45°-67°")
        draw_arrows("east")

    elif (heading <= DEGREES_SE and heading >= (DEGREES_SE - 23)) or (
        heading >= DEGREES_SE and heading <= (DEGREES_SE + 23)
    ):
        print("INFO: SOUTH EAST is between 23°-45°, 45°-67°")
        draw_arrows("south-east")

    elif (heading <= DEGREES_S and heading >= (DEGREES_S - 22)) or (
        heading >= DEGREES_S and heading <= (DEGREES_S + 22)
    ):
        print("INFO: SOUTH is between 203°-180°, 180°-158°")
        draw_arrows("south")

    elif (heading >= DEGREES_SW and heading <= (DEGREES_SW + 23)) or (
        heading <= DEGREES_SW and heading >= (DEGREES_SW - 23)
    ):
        print("INFO: SOUTH WEST is between 292°-270°, 270°-248°")
        draw_arrows("south-west")

    elif (heading >= DEGREES_W and heading <= (DEGREES_W + 22)) or (
        heading <= DEGREES_W and heading >= (DEGREES_W - 22)
    ):
        print("INFO: WEST is between 292°-270°, 270°-248°")
        draw_arrows("west")

    elif (heading >= DEGREES_NW and heading <= (DEGREES_NW + 23)) or (
        heading <= DEGREES_NW and heading >= (DEGREES_NW - 23)
    ):
        print("INFO: NORTH WEST is between 292°-270°, 270°-248°")
        draw_arrows("north-west")

    sleep(1000)
