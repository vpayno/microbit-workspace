# Imports go at the top
import music
from microbit import *


class Icons:
    """Various application icons."""

    ARROW_UP: Image = Image.ARROW_N
    ARROW_RT: Image = Image.ARROW_E
    ARROW_LT: Image = Image.ARROW_W
    ARROW_DN: Image = Image.ARROW_S

    LOGO: Image = Image(
        "09990:"
        "90609:"
        "90809:"
        "90069:"
        "09990:"
    )  # fmt: off

    PAUSE: Image = Image(
        "00000:"
        "09090:"
        "09090:"
        "09090:"
        "00000:"
    )  # fmt: off

    # tried to make two overlapping arrows, looks more like a candy wrapper
    CANDY: Image = Image(
        "09000:"
        "99990:"
        "09090:"
        "09999:"
        "00090:"
    )  # fmt: off

    # looks like a copyright C
    SECOND_UNIT: Image = Image(
        "66666:"
        "60996:"
        "69006:"
        "60996:"
        "66666:"
    )  # fmt: off

    # looks like an H
    MINUTE_UNIT: Image = Image(
        "66666:"
        "69096:"
        "69696:"
        "69096:"
        "66666:"
    )  # fmt: off

    # looks like an h
    HOUR_UNIT: Image = Image(
        "66666:"
        "69006:"
        "69996:"
        "69096:"
        "66666:"
    )  # fmt: off


class Wheel:
    """Manages images of a spinning wheel."""

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
        """Returns the next image in the self.wheel animation."""

        self.wheel_index = (self.wheel_index + 1) % len(self.wheels)

        return self.wheels[self.wheel_index]


class Timer:
    """Simple timer experiment."""

    def __init__(self) -> None:
        self.icons = Icons()

        # first button selection starts at the second index
        # all of these are sorted h -> s -> m
        self.units: "list[str]" = ["h", "s", "m"]
        self.unit_multipliers: "list[int]" = [60 * 60, 1, 60]
        self.duration_limits: "list[int]" = [24, 90, 90]

        # first button selection starts at the second index
        self.offsets: "list[int]" = [45, 1, 5, 10, 30]

        # annotations are limited, using zero values instead of None
        self.duration: int = 0
        self.unit: str = "x"
        self.time_remaining: int = 0
        self.offset: int = 0

        self.units_index: int = 0
        self.duration_index: int = 0
        self.offset_index: int = 0

        self.units_selected: bool = False
        self.duration_selected: bool = False

        display.show(self.icons.LOGO)
        sleep(2_000)

        self.reset_button_events()

    def reset_button_events(self) -> None:
        """Helps prevent button press stacking."""

        button_a.was_pressed()
        button_b.was_pressed()

    def select_units(self) -> None:
        """UI to select the timer duration units."""

        print("INFO: selecting self.units")
        while not self.units_selected or self.unit == "x":
            if self.unit != "x":
                display.show(self.icons.ARROW_RT)
                sleep(500)

            display.show(self.icons.ARROW_LT)
            sleep(500)

            if self.unit != "x":
                display.scroll("u:" + self.unit)

            if button_a.was_pressed():
                self.reset_button_events()
                self.units_index = (self.units_index + 1) % len(self.units)
                self.unit = self.units[self.units_index]
                print("INFO: selected self.units: " + self.unit)
                display.show(self.units[self.units_index])
                sleep(1_000)

            b_pressed: bool = button_b.was_pressed()

            if b_pressed and self.unit != "x":
                self.reset_button_events()
                self.units_selected = True
                print("INFO: self.units confirmed")
                display.show("u:" + self.unit)
                sleep(1_000)
                display.show(Image.YES)
                sleep(1_000)
            elif b_pressed:
                self.reset_button_events()
                print("ERROR: must select a valid time self.unit")
                display.show(Image.NO)
                sleep(1_000)

    def select_duration(self) -> None:
        """UI to select the timer duration."""

        print("INFO: selecting self.duration in " + self.unit)
        while not self.duration_selected:
            display.show(self.icons.ARROW_UP)
            sleep(1_000)

            if self.offset != 0 and self.duration != 0:
                display.show(self.icons.ARROW_RT)
                sleep(1_000)

            if self.offset != 0:
                display.show(self.icons.ARROW_LT)
                sleep(1_000)

            if self.offset != 0 and self.duration != 0:
                display.scroll("d:" + str(self.duration) + " o:" + str(self.offset))

            if pin_logo.is_touched():
                self.offset_index = (self.offset_index + 1) % len(self.offsets)
                self.offset = self.offsets[self.offset_index]
                print("INFO: new self.duration selection self.offset is " + str(self.offset))
                display.scroll("+" + str(self.offset))
                sleep(1_000)

            if button_a.was_pressed() and self.offset != 0:
                self.reset_button_events()
                self.duration = (self.duration + self.offset) % self.duration_limits[self.units_index]
                print(
                    "INFO: self.duration: " + str(self.duration) + self.unit + " (self.offset=" + str(self.offset) + ")"
                )
                display.scroll(str(self.duration) + self.unit)
                sleep(1_000)

            b_pressed: bool = button_b.was_pressed()
            self.reset_button_events()

            if b_pressed and (self.offset != 0 or self.duration != 0):
                if self.duration != 0:
                    self.duration_selected = True
                    self.time_remaining = self.duration * self.unit_multipliers[self.units_index]
                    print("INFO: self.duration confirmed")
                    display.scroll("t:" + str(self.duration) + self.unit)
                    sleep(1_000)
                    display.show(Image.YES)
                    sleep(1_000)
            elif b_pressed and (self.offset == 0 or self.duration == 0):
                print("ERROR: must select a positive self.offset and self.duration")
                display.show(Image.NO)
                sleep(1_000)

    def prompt_to_start_timer(self) -> None:
        """UI for the user to start the timer."""

        self.reset_button_events()
        display.show(Image.ARROW_E)
        print("INFO: waiting on button b press to start timer")
        hold: bool = True
        while hold:
            if button_a.was_pressed():
                print("INFO: timer was canceled")
                display.show(Image.NO)
                sleep(1_000)
                reset()  # probably canceled because the settings are wrong, start over

            if button_b.was_pressed():
                hold = False
                print("INFO: timer started")
                display.show(Image.YES)
                sleep(500)

    def run_timer(self) -> None:
        """The running timer."""

        warn_at: int = int(self.time_remaining * 0.10)

        print("INFO: starting timer of " + str(self.duration) + self.units[self.units_index])
        print("INFO: 10% waring time: " + str(warn_at) + " seconds")

        self.wheel = Wheel()
        while self.time_remaining > 0:
            print("INFO: time left: " + str(self.time_remaining) + " seconds")
            display.show(self.wheel.turn())
            sleep(1_000)

            if warn_at == self.time_remaining:
                print("INFO: playing 10% waring sound")
                music.play(music.BADDY)
                sleep(500)

            self.time_remaining -= 1

            if button_a.was_pressed():
                print("INFO: timer was aborted")
                display.show(Image.NO)
                sleep(1_000)
                self.time_remaining = -1

            if button_b.was_pressed():
                print("INFO: timer paused")
                display.show(self.icons.PAUSE)
                print("INFO: waiting on button b press to unpause timer")
                while not button_b.was_pressed():
                    sleep(500)
                print("INFO: timer resuming...")
                display.show(Image.YES)
                sleep(500)
                _ = button_a.was_pressed()  # reset button_a only to prevent accidental cancel

        print("INFO: timer completed")
        display.show(Image.FABULOUS)
        music.play(music.DADADADUM)

    def reset_options(self) -> None:
        """Resets timer options."""

        display.show(Image.NO)
        sleep(1_000)
        reset()  # probably canceled because the settings are wrong, start over

        if button_b.was_pressed():
            print("INFO: timer started")
            display.show(Image.YES)
            sleep(500)

    def reset_state(self) -> None:
        """Resets timer options."""

        self.units_selected = False
        self.duration_selected = False

    def run(self) -> None:
        """Runs the timer."""

        self.select_units()
        self.select_duration()
        self.prompt_to_start_timer()
        self.run_timer()
        self.reset_state()


print()
print("INFO: Microbit Timer")
print()

app: Timer = Timer()

# Code in a 'while True:' loop repeats forever
while True:
    app.run()

    sleep(10_000)
