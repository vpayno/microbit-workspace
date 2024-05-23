# Imports go at the top
from microbit import *


class EntropyMeter:
    """Accidentally discovered that the accelerometer always returns data even when idle."""

    def __init__(self) -> None:
        self.dot: "tuple[int, int, int]" = (0, 0, 0)
        self.data: "tuple[int, int, int]" = (0, 0, 0)

        self.direction: float = 0.0

    def run(self) -> None:
        """
        1. Gets "entropy" data (the accelerometer is never "idle")
        2. Use the data to draw a dot.
        """

        self.data = accelerometer.get_values()
        print("INFO: data=" + str(self.data))

        # x, y, brightness
        self.dot = (abs(self.data[0] % 5), abs(self.data[1] % 5), abs(self.data[2] % 10))
        print("INFO:  dot=" + str(self.dot))
        display.set_pixel(*self.dot)


print()
print("Entropy Meter")
print()

display.on()
display.clear()

app: EntropyMeter = EntropyMeter()

# Code in a 'while True:' loop repeats forever
while True:
    app.run()

    sleep(1_000)
