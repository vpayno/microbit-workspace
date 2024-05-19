# Imports go at the top

import music
import radio
from microbit import *


class Wheel:
    wheel0: Image = Image(
        "00900:"
        "00900:"
        "00900:"
        "00900:"
        "00900:"
    )  # fmt: off
    wheel4 = wheel0

    wheel1: Image = Image(
        "00009:"
        "00090:"
        "00900:"
        "09000:"
        "90000:"
    )  # fmt: off
    wheel5 = wheel1

    wheel2: Image = Image(
        "00000:"
        "00000:"
        "99999:"
        "00000:"
        "00000:"
    )  # fmt: off
    wheel6 = wheel2

    wheel3: Image = Image(
        "90000:"
        "09000:"
        "00900:"
        "00090:"
        "00009:"
    )  # fmt: off
    wheel7 = wheel3

    def __init__(self) -> None:
        self.wheel_index: int = 0
        self.wheels: "list[Image]" = [
            self.wheel0,
            self.wheel1,
            self.wheel2,
            self.wheel3,
            self.wheel4,
            self.wheel5,
            self.wheel6,
            self.wheel7,
        ]

    def turn(self) -> Image:
        self.wheel_index = (self.wheel_index + 1) % len(self.wheels)
        return self.wheels[self.wheel_index]


class Icons:
    ARROW_UP: Image = Image.ARROW_N
    ARROW_RT: Image = Image.ARROW_E
    ARROW_LT: Image = Image.ARROW_W
    ARROW_DN: Image = Image.ARROW_S

    # offset H & C
    LOGO1: Image = Image(
        "90900:"
        "99900:"
        "90999:"
        "00900:"
        "00999:"
    )  # fmt: off

    # HC
    LOGO2: Image = Image(
        "00000:"
        "90999:"
        "99900:"
        "90999:"
        "00000:"
    )  # fmt: off


class HighCard:
    """Uses the radio to text data."""

    USE_RUNES: bool = True

    runes: "list[int]" = list(range(0, 10))  # 0..9

    def __init__(self) -> None:
        """Setup the initial state but don't enable the radio."""

        self.group: int = -1
        self.group_size: int = 256
        self.group_offset: int = 8  # random.choice(prime_numbers)

        self.power_max: int = 7

        # print("INFO: selected prime [" + str(self.group_offset) + "]")

        self.rune_index: int = -1
        self.runes_size: int = len(self.runes)
        self.rune_offset: int = 1
        self.rune_name: str = ""
        self.rune_value: int = -1

        print("INFO: images=" + str(self.runes) + "(" + str(self.runes_size) + ")")

    def setup(self) -> None:
        """Enable radio, select group and message."""

        radio.on()
        print("INFO: enabled radio")

        self.group_browse()
        self.rune_browse()

    def group_browse(self) -> None:
        """Helps the user select the 'radio frequency'."""

        display.scroll("group")
        sleep(500)

        selected_group: bool = False

        while not selected_group:
            display.show(Image.ARROW_E)
            sleep(500)
            display.show(self.group if self.group in range(0, self.group_size) else "G")
            sleep(500)
            display.show(Image.ARROW_W)
            sleep(500)

            if button_b.was_pressed():
                self.group = (max(self.group, 0) + self.group_offset) % self.group_size
                print("INFO: current group [" + str(self.group) + "]")
                display.scroll(self.group)

            if button_a.was_pressed():
                self.group = (max(self.group, 0) - self.group_offset) % self.group_size
                print("INFO: current group [" + str(self.group) + "]")
                display.scroll(self.group)

            if pin_logo.is_touched() and self.group >= 0:
                selected_group = True
                display.show(Image.YES)
                sleep(1_000)

        print("INFO: selected group [" + str(self.group) + "]")
        display.scroll("g:" + str(self.group))

        print("INFO: config group [" + str(self.group) + "]")
        print("INFO: config power [" + str(self.power_max) + "]")
        radio.config(group=self.group, power=self.power_max)

        sleep(1_000)

    def rune_browse(self) -> None:
        """Browe available runes to send as a message."""

        display.scroll("card")  # less confusing for users than "runes"
        sleep(500)

        self.rune_index: int = -1
        self.rune_name: str = ""
        self.rune_value: int = -1

        selected_rune: bool = False

        while not selected_rune:
            display.show(Image.ARROW_E)
            sleep(500)
            display.show(self.rune_value if self.rune_value in self.runes else "c")
            sleep(500)
            display.show(Image.ARROW_W)
            sleep(500)

            if button_b.was_pressed():
                self.rune_index = (max(self.rune_index, 0) + self.rune_offset) % self.runes_size
                self.rune_value = self.runes[self.rune_index]
                self.rune_name = str(self.rune_value)
                print("INFO: current rune [" + self.rune_name + "]")
                display.show(self.runes[self.rune_index])
                sleep(500)

            if button_a.was_pressed():
                self.rune_index = (max(self.rune_index, 0) - self.rune_offset) % self.runes_size
                self.rune_value = self.runes[self.rune_index]
                self.rune_name = str(self.rune_value)
                print("INFO: current rune [" + self.rune_name + "]")
                display.show(self.rune_name)
                sleep(500)

            if pin_logo.is_touched() and self.rune_index >= 0:
                selected_rune = True
                display.show(Image.YES)
                sleep(1_000)

        print("INFO: selected rune [" + self.rune_name + "]")
        display.scroll("c:" + self.rune_name)
        sleep(1_000)

        self.message: str = self.rune_name

    def run(self) -> None:
        """Runs the send/receive loop."""

        response: "str | None" = "None"

        print("INFO: starting send/receive loop")

        wheel: Wheel = Wheel()

        while response == "None" or response is None:
            display.show(wheel.turn())
            radio.send(self.message)
            print("INFO: sent message [" + self.message + "]")
            sleep(500)
            response = radio.receive()
            print("INFO: tentative response [" + str(response) + "]")
            sleep(500)

        self.response: str = str(response)
        print("INFO: accepted response [" + self.response + "]")

    def score_game(self) -> int:
        """Score a game of RPS

        9 > 0

        :return: 2 if local player won, 1 if tied, 0 if lost
        """

        # enums would be nice here
        # lost:0, tied:1, won:2
        result: int = 0

        if self.message == self.response:
            # display.scroll(self.message + "==" + self.response)
            display.scroll("tie")
            result = 1

        elif self.message > self.response:
            display.scroll(self.message + ">" + self.response)
            display.scroll("won")
            result = 2

        else:
            display.scroll(self.message + "<" + self.response)
            display.scroll("lost")

        print("INFO: you played [" + self.message + "] against [" + self.response + "]")
        print("INFO: you " + "won!" if result == 2 else "tied!" if result == 1 else "lost!")  # lol

        sleep(1_000)

        return result


def reset_button_events() -> None:
    _ = button_a.was_pressed()
    _ = button_b.was_pressed()


def wait_on_any_button() -> None:
    print("INFO: Waiting on any-key press")
    reset_button_events()
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1_000)
    reset_button_events()
    print("INFO: any-key pressed")


print()
print("High Card Game")
print()

icons = Icons()
display.show(icons.LOGO1)
sleep(1_000)

print("INFO: playing music.ENTERTAINER")
music.play(music.ENTERTAINER)

app: HighCard = HighCard()
app.setup()

# Code in a 'while True:' loop repeats forever
while True:
    app.run()

    score: int = app.score_game()

    if score == 2:
        display.show("W")
        music.play(music.BA_DING)
    elif score == 1:
        display.show("T")
        music.play(music.PUNCHLINE)
    else:
        display.show("L")
        music.play(music.WAWAWAWAA)

    wait_on_any_button()

    app.rune_browse()
