# Imports go at the top
import random

from microbit import *


def roll_dice(sides: int = 6) -> int:
    return random.randint(1, sides)


def was_shaken() -> bool:
    if accelerometer.was_gesture("shake"):
        print("INFO: shaken, not stirred")

        strength: int = accelerometer.get_strength()

        print("INFO: force used to shake was " + str(strength))

        # let's try to keep users from breaking the microbit dice
        # looks like max value is < 3,500
        # average shake is around 1,000
        if strength > 2_000:
            print("WARN: you risk angering the RNG gods!")
            display.show(Image.ANGRY)
            sleep(2000)

        return True

    return False


def was_touched() -> bool:
    if pin_logo.is_touched():
        print("INFO: touched, not shaken")

        return True

    return False


# at first glance, it looks like the pin_logo is a bad idea but it
# blocks the execution of the code so it's only rolling dice and you
# don't see the roll until after you release the pin
def was_roll_requested() -> bool:
    return was_shaken() or was_touched()


faces: list = [4, 6, 8, 12, 20]
face_index: int = 0
sides: int = faces[face_index]
roll: int = 0

print("INFO: sides:" + str(sides) + " roll:" + str(roll))

# Code in a 'while True:' loop repeats forever
while True:
    while not was_roll_requested():
        display.scroll(str(roll))

        # decrement sides
        presses_a: int = button_a.get_presses()
        if presses_a > 0:
            face_index = (face_index - 1) % len(faces)
            sides = faces[face_index]
            print("INFO: new number of sides is " + str(sides))

            # this adds latency to the button feedback
            display.show(str(sides))
            sleep(500)

        # increment sides
        presses_b: int = button_b.get_presses()
        if presses_b > 0:
            face_index = (face_index + 1) % len(faces)
            sides = faces[face_index]
            print("INFO: new number of sides is " + str(sides))

            # this adds latency to the button feedback
            display.show(str(sides))
            sleep(500)

    print("INFO: rolling dice...")

    roll = roll_dice(sides)

    # closest thing to a spinning wheel
    # this was a good call, it adds suspense and feed back so you
    # know when it was shaken or when you can let go of the pin_logo
    display.show(Image.ALL_CLOCKS)

    print("INFO: sides:" + str(sides) + " roll:" + str(roll))
