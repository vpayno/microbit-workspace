# Imports go at the top
import music
from microbit import *


class Icons:
    ARROW_UP: Image = Image.ARROW_N
    ARROW_RT: Image = Image.ARROW_E
    ARROW_LT: Image = Image.ARROW_W
    ARROW_DN: Image = Image.ARROW_S

    LOGO: Image = Image("09990:" "90609:" "90809:" "90069:" "09990:")

    PAUSE: Image = Image("00000:" "09090:" "09090:" "09090:" "00000:")

    # tried to make two overlapping arrows, looks more like a candy wrapper
    CANDY: Image = Image("09000:" "99990:" "09090:" "09999:" "00090:")

    # looks like a copyright C
    SECOND_UNIT: Image = Image("66666:" "60996:" "69006:" "60996:" "66666:")

    # looks like an H
    MINUTE_UNIT: Image = Image("66666:" "69096:" "69696:" "69096:" "66666:")

    # looks like an h
    HOUR_UNIT: Image = Image("66666:" "69006:" "69996:" "69096:" "66666:")


class Wheel:
    wheel0: Image = Image("00900:" "00900:" "00900:" "00900:" "00900:")
    wheel4 = wheel0

    wheel1: Image = Image("00009:" "00090:" "00900:" "09000:" "90000:")
    wheel5 = wheel1

    wheel2: Image = Image("00000:" "00000:" "99999:" "00000:" "00000:")
    wheel6 = wheel2

    wheel3: Image = Image("90000:" "09000:" "00900:" "00090:" "00009:")
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


def reset_button_events() -> None:
    button_a.was_pressed()
    button_b.was_pressed()


icons = Icons()

print("INFO: Microbit Timer")

# first button selection starts at the second index
# all of these are sorted h -> s -> m
units: "list[str]" = ["h", "s", "m"]
unit_multipliers: "list[int]" = [60 * 60, 1, 60]
duration_limits: "list[int]" = [24, 90, 90]

# first button selection starts at the second index
offsets: "list[int]" = [45, 1, 5, 10, 30]

# annotations are limited, using zero values instead of None
duration: int = 0
unit: str = "x"
time_remaining: int = 0
offset: int = 0

units_index: int = 0
duration_index: int = 0
offset_index: int = 0

units_selected: bool = False
duration_selected: bool = False

display.show(icons.LOGO)
sleep(2_000)

reset_button_events()


# Code in a 'while True:' loop repeats forever
while True:
    print("INFO: selecting units")
    while not units_selected or unit == "x":
        if unit != "x":
            display.show(icons.ARROW_RT)
            sleep(500)

        display.show(icons.ARROW_LT)
        sleep(500)

        if unit != "x":
            display.scroll("u:" + unit)

        if button_a.was_pressed():
            reset_button_events()
            a_pressed_once = True
            units_index = (units_index + 1) % len(units)
            unit = units[units_index]
            print("INFO: selected units: " + unit)
            display.show(units[units_index])
            sleep(1_000)

        b_pressed: bool = button_b.was_pressed()

        if b_pressed and unit != "x":
            reset_button_events()
            units_selected = True
            print("INFO: units confirmed")
            display.show("u:" + unit)
            sleep(1_000)
            display.show(Image.YES)
            sleep(1_000)
        elif b_pressed:
            reset_button_events()
            print("ERROR: must select a valid time unit")
            display.show(Image.NO)
            sleep(1_000)

    print("INFO: selecting duration in " + unit)
    while not duration_selected:
        display.show(icons.ARROW_UP)
        sleep(1_000)

        if offset != 0 and duration != 0:
            display.show(icons.ARROW_RT)
            sleep(1_000)

        if offset != 0:
            display.show(icons.ARROW_LT)
            sleep(1_000)

        if offset != 0 and duration != 0:
            display.scroll("d:" + str(duration) + " o:" + str(offset))

        if pin_logo.is_touched():
            pin_pressed_once = True
            offset_index = (offset_index + 1) % len(offsets)
            offset = offsets[offset_index]
            print("INFO: new duration selection offset is " + str(offset))
            display.scroll("+" + str(offset))
            sleep(1_000)

        if button_a.was_pressed() and offset != 0:
            reset_button_events()
            duration = (duration + offset) % duration_limits[units_index]
            print("INFO: duration: " + str(duration) + unit + " (offset=" + str(offset) + ")")
            display.scroll(str(duration) + unit)
            sleep(1_000)

        b_pressed: bool = button_b.was_pressed()
        reset_button_events()

        if b_pressed and (offset != 0 or duration != 0):
            if duration != 0:
                duration_selected = True
                time_remaining = duration * unit_multipliers[units_index]
                print("INFO: duration confirmed")
                display.scroll("t:" + str(duration) + unit)
                sleep(1_000)
                display.show(Image.YES)
                sleep(1_000)
        elif b_pressed and (offset == 0 or duration == 0):
            print("ERROR: must select a positive offset and duration")
            display.show(Image.NO)
            sleep(1_000)

    reset_button_events()
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

    warn_at: int = int(time_remaining * 0.10)

    print("INFO: starting timer of " + str(duration) + units[units_index])
    print("INFO: 10% waring time: " + str(warn_at) + " seconds")

    wheel = Wheel()
    while time_remaining > 0:
        print("INFO: time left: " + str(time_remaining) + " seconds")
        display.show(wheel.turn())
        sleep(1_000)

        if warn_at == time_remaining:
            print("INFO: playing 10% waring sound")
            music.play(music.BADDY)
            sleep(500)

        time_remaining -= 1

        if button_a.was_pressed():
            print("INFO: timer was aborted")
            display.show(Image.NO)
            sleep(1_000)
            time_remaining = -1

        if button_b.was_pressed():
            print("INFO: timer paused")
            display.show(icons.PAUSE)
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
    sleep(10_000)

    units_selected = False
    duration_selected = False
