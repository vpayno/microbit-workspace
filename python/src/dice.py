# Imports go at the top
import random

from microbit import *


class Dice:
    """Simulates a single dice."""

    def __init__(self) -> None:
        self.faces: list = [4, 6, 8, 12, 20]
        self.face_index: int = 0
        self.sides: int = self.faces[self.face_index]
        self.roll: int = 0

        print("INFO: sides:" + str(self.sides) + " roll:" + str(self.roll))

    def roll_dice(self) -> None:
        """Throw the dice and return it's value."""

        self.roll = random.randint(1, self.sides)

        print("INFO: sides:" + str(self.sides) + " roll:" + str(self.roll))

    def was_shaken(self) -> bool:
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

    def was_touched(self) -> bool:
        if pin_logo.is_touched():
            print("INFO: touched, not shaken")

            return True

        return False

    def was_roll_requested(self) -> bool:
        """
        at first glance, it looks like the pin_logo is a bad idea but it
        blocks the execution of the code so it's only rolling dice and you
        don't see the roll until after you release the pin
        """

        return self.was_shaken() or self.was_touched()

    def scroll_sides_left(self) -> None:
        """Scrolls left on the list of predefined sides."""

        self.face_index = (self.face_index - 1) % len(self.faces)
        self.sides = self.faces[self.face_index]
        print("INFO: new number of sides is " + str(self.sides))

        # this adds latency to the button feedback
        display.show(str(self.sides))

    def scroll_sides_right(self) -> None:
        """Scrolls right on the list of predefined sides."""

        self.face_index = (self.face_index + 1) % len(self.faces)
        self.sides = self.faces[self.face_index]
        print("INFO: new number of sides is " + str(self.sides))

        # this adds latency to the button feedback
        display.show(str(self.sides))


print()
print("Dice Simulator")
print()

dice: Dice = Dice()

# Code in a 'while True:' loop repeats forever
while True:
    while not dice.was_roll_requested():
        display.scroll(str(dice.roll))

        # decrement sides
        presses_a: int = button_a.get_presses()
        if presses_a > 0:
            dice.scroll_sides_left()
            sleep(500)

        # increment sides
        presses_b: int = button_b.get_presses()
        if presses_b > 0:
            dice.scroll_sides_right()
            sleep(500)

    print("INFO: rolling dice...")

    dice.roll_dice()

    # closest thing to a spinning wheel
    # this was a good call, it adds suspense and feed back so you
    # know when it was shaken or when you can let go of the pin_logo
    display.show(Image.ALL_CLOCKS)
