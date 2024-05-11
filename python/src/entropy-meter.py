# Imports go at the top
from microbit import *

dot: "tuple[int, int, int]" = (0, 0, 0)
data: "tuple[int, int, int]" = (0, 0, 0)

direction: float = 0.0
display.on()
display.clear()

# Code in a 'while True:' loop repeats forever
while True:
    data = accelerometer.get_values()
    print("INFO: data=" + str(data))

    # x, y, brightness
    dot = (abs(data[0] % 5), abs(data[1] % 5), abs(data[2] % 10))
    print("INFO:  dot=" + str(dot))
    display.set_pixel(*dot)

    sleep(1000)
