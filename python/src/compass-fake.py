# Imports go at the top
from microbit import *


class Compass:
    """Fake Compass"""

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

        print("INFO: If you don't see any output, please calibrate the compass.")

    def run(self) -> None:
        """
        1. Probe compass
        2. Draw arrow
        """

        # this call will make you play fill the screen/dots to calibrate
        # the compas - when it's ready it will display a smily face
        self.heading = compass.heading()
        print("INFO: self.heading: " + str(self.heading) + "°")

        if (self.heading >= self.DEGREES_N and self.heading <= (self.DEGREES_N + 22)) or (
            self.heading <= self.DEGREES_N_ALT and self.heading >= (self.DEGREES_N_ALT - 22)
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


app: Compass = Compass()


# Code in a 'while True:' loop repeats forever
while True:
    app.run()
    sleep(1_000)
