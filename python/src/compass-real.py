# Imports go at the top
from microbit import *


class Compass:
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
        self.heading: int
        self.bearing: str

        print("If you don't see any output, please calibrate the compass.")

    def run(self) -> None:
        # this call will make you play fill the screen/dots to calibrate
        # the compas - when it's ready it will display a smily face
        self.heading = compass.heading()
        print("INFO: self.heading: " + str(self.heading) + "°")

        if (self.heading >= self.DEGREES_N and self.heading <= (self.DEGREES_N + 22)) or (
            self.heading <= self.DEGREES_N_ALT and self.heading >= (self.DEGREES_N_ALT - 22)
        ):
            print("INFO: NORTH is between 337°-360°, 0°-22°")
            self.bearing = "north"

        elif (self.heading <= self.DEGREES_NE and self.heading >= (self.DEGREES_NE - 23)) or (
            self.heading >= self.DEGREES_NE and self.heading <= (self.DEGREES_NE + 23)
        ):
            print("INFO: NORTH EAST is between 23°-45°, 45°-67°")
            self.bearing = "north-east"

        elif (self.heading <= self.DEGREES_E and self.heading >= (self.DEGREES_E - 22)) or (
            self.heading >= self.DEGREES_E and self.heading <= (self.DEGREES_E + 22)
        ):
            print("INFO: EAST is between 23°-45°, 45°-67°")
            self.bearing = "east"

        elif (self.heading <= self.DEGREES_SE and self.heading >= (self.DEGREES_SE - 23)) or (
            self.heading >= self.DEGREES_SE and self.heading <= (self.DEGREES_SE + 23)
        ):
            print("INFO: SOUTH EAST is between 23°-45°, 45°-67°")
            self.bearing = "south-east"

        elif (self.heading <= self.DEGREES_S and self.heading >= (self.DEGREES_S - 22)) or (
            self.heading >= self.DEGREES_S and self.heading <= (self.DEGREES_S + 22)
        ):
            print("INFO: SOUTH is between 203°-180°, 180°-158°")
            self.bearing = "south"

        elif (self.heading >= self.DEGREES_SW and self.heading <= (self.DEGREES_SW + 23)) or (
            self.heading <= self.DEGREES_SW and self.heading >= (self.DEGREES_SW - 23)
        ):
            print("INFO: SOUTH WEST is between 292°-270°, 270°-248°")
            self.bearing = "south-west"

        elif (self.heading >= self.DEGREES_W and self.heading <= (self.DEGREES_W + 22)) or (
            self.heading <= self.DEGREES_W and self.heading >= (self.DEGREES_W - 22)
        ):
            print("INFO: WEST is between 292°-270°, 270°-248°")
            self.bearing = "west"

        elif (self.heading >= self.DEGREES_NW and self.heading <= (self.DEGREES_NW + 23)) or (
            self.heading <= self.DEGREES_NW and self.heading >= (self.DEGREES_NW - 23)
        ):
            print("INFO: NORTH WEST is between 292°-270°, 270°-248°")
            self.bearing = "north-west"

        self.draw_arrows()

    def draw_arrows(self) -> None:
        display.clear()

        self.north_arrow()
        self.south_arrow()
        self.west_arrow()
        self.east_arrow()

    def north_arrow(self) -> None:
        # 0,0 -> top-left corner
        column: int = 0
        row: int = 0
        brightness: int = 9

        if self.bearing == "north":
            column = 2
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column, row + 1, brightness - 3)
            display.set_pixel(column, row + 2, brightness - 6)

        elif self.bearing == "north-east":
            column = 0
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column + 1, row + 1, brightness - 3)
            display.set_pixel(column + 2, row + 2, brightness - 6)

        elif self.bearing == "east":
            column = 0
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column + 1, row, brightness - 3)
            display.set_pixel(column + 2, row, brightness - 6)

        elif self.bearing == "south-east":
            column = 0
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column + 1, row - 1, brightness - 3)
            display.set_pixel(column + 2, row - 2, brightness - 6)

        elif self.bearing == "south":
            column = 2
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column, row - 1, brightness - 3)
            display.set_pixel(column, row - 2, brightness - 6)

        elif self.bearing == "south-west":
            column = 4
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column - 1, row - 1, brightness - 3)
            display.set_pixel(column - 2, row - 2, brightness - 6)

        elif self.bearing == "west":
            column = 4
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column - 1, row, brightness - 3)
            display.set_pixel(column - 2, row, brightness - 6)

        elif self.bearing == "north-west":
            column = 4
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)
            display.set_pixel(column - 1, row + 1, brightness - 3)
            display.set_pixel(column - 2, row + 2, brightness - 6)

    def south_arrow(self) -> None:
        # 0,0 -> top-left corner
        column: int = 0
        row: int = 0
        brightness: int = 9 - 3

        if self.bearing == "north":
            column = 2
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "north-east":
            column = 4
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "east":
            column = 4
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south-east":
            column = 4
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south":
            column = 2
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south-west":
            column = 0
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "west":
            column = 0
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "north-west":
            column = 0
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

    def west_arrow(self) -> None:
        # 0,0 -> top-left corner
        column: int = 0
        row: int = 0
        brightness: int = 9 - 6

        if self.bearing == "north":
            column = 0
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "north-east":
            column = 0
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "east":
            column = 2
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south-east":
            column = 4
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south":
            column = 4
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south-west":
            column = 4
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "west":
            column = 2
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "north-west":
            column = 0
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

    def east_arrow(self) -> None:
        # 0,0 -> top-left corner
        column: int = 0
        row: int = 0
        brightness: int = 9 - 6

        if self.bearing == "north":
            column = 4
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "north-east":
            column = 4
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "east":
            column = 2
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south-east":
            column = 0
            row = 0
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south":
            column = 0
            row = 2
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "south-west":
            column = 0
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "west":
            column = 2
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)

        elif self.bearing == "north-west":
            column = 4
            row = 4
            # column (0..4), row (0..4), brightness (0..9)
            display.set_pixel(column, row, brightness)


app: Compass = Compass()

# Code in a 'while True:' loop repeats forever
while True:
    app.run()
    sleep(1_000)
