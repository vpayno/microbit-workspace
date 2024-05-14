# Imports go at the top
from math import ceil

import music
from microbit import *


# Pomodoro Timer Class
class Pomodoro:
    def __init__(self, work_duration: int = 45, break_duration: int = 15) -> None:
        """
        :param work_duration: the length, in minutes, of the work timer
        :param break_duration: the length, in minutes, of the break timer
        """

        self.time_left: int = 0
        self.work_duration: int = work_duration
        self.break_duration: int = break_duration
        self.second: int = 1_000
        self.warned: bool = False

    def _five_minute_warning(self, fives_left: int) -> None:
        """Private method used to issue the five minute warnings.

        :param fives_left: the number of 5 minute chunks left in the running timer.
        """

        if fives_left == 1 and not self.warned and (self.work_duration > 5 or self.break_duration > 5):
            music.play(music.BADDY)

            if self.time_left <= 5:
                self.warned = not self.warned

    def _run_timer(self, name: str, duration: int) -> bool:
        """Runs the internal timer

        :param name: work or break
        :param duration: in minutes
        :return: true, completed | false, canceled
        """

        print("INFO: starting " + name + " timer for " + str(self.work_duration) + " minutes")

        self.time_left = duration

        while self.time_left > 0:
            print("INFO: " + str(self.time_left) + " minutes left in " + name + " timer")

            # there are 12 fives in an hour, we can use that to
            # show timer progress in a non-distracting way
            fives: int = int(ceil((self.time_left % 60) / 5))
            clock_name: str = "CLOCK" + str(fives)

            print("INFO: showing clock face -> " + clock_name)
            display.show(getattr(Image, clock_name))

            self._five_minute_warning(fives)

            self.time_left -= 1

            heartbeat: bool = True
            count: int = 60

            # counts seconds in a minute
            while count > 0:
                if heartbeat:
                    display.set_pixel(2, 2, 8)
                else:
                    display.set_pixel(2, 2, 4)
                heartbeat = not heartbeat

                count -= 1
                sleep(self.second)

                if button_b.was_pressed():
                    reset_button_states()

                    print("INFO: button_b pressed, pausing timer until button_a pressed")
                    display.show(Image.ARROW_W)

                    while not button_a.was_pressed():
                        sleep(1000)

                    reset_button_states()

                    print("INFO: button_a pressed, unpausing")
                    display.show(getattr(Image, clock_name))

                if button_a.was_pressed():
                    reset_button_states()

                    print("INFO: button_a was pressed, canceling timer")
                    display.show(Image.NO)
                    sleep(2000)

                    return False

        return True

    def start_timer(self) -> None:
        """Starts the timer and handles led and audio notifications."""

        status: bool = self._run_timer("work", self.work_duration)

        if status:
            print("INFO: work timer completed")
            display.show(Image.SMILE)
            audio.play(Sound.HAPPY)
            sleep(1000)

            if self._run_timer("break", self.break_duration):
                print("INFO: break timer completed")
                display.show(Image.FABULOUS)
                sleep(1000)
            else:
                print("INFO: break timer canceled")

        else:
            print("INFO: work timer canceled")


# Helper functions


def reset_button_states() -> None:
    """We need to read buttons again after reading them to make sure
    that users can't stack button presses."""

    _ = button_a.was_pressed()
    _ = button_b.was_pressed()


def wait_for_pin_logo(selected: int, durations: "list[tuple[int, int]]") -> int:
    """Waits for the user to start the timer by pressing the pin_logo button
    and also gives the user the opportunity to change the timer defaults.

    :param selected: the index of the duration tuple selected from the list
    :param durations: the list of timer tuples
    :return: the selected index
    """

    print("INFO: waiting on pin_logo press")

    while not pin_logo.is_touched():
        display.show(Image.ARROW_N)
        sleep(500)
        display.show(Image.ARROW_W)
        sleep(500)

        # sleep(1000)
        # display.show(Image.ALL_ARROWS)

        if button_a.was_pressed():
            reset_button_states()
            selected = (selected + 1) % len(durations)

            print("INFO: selected timer -> " + str(durations[selected]))
            display.scroll(str(durations[selected]))
            sleep(500)

            display.show(Image.ARROW_N)

    return selected


# defaults to 45:15
durations: "list[tuple[int, int]]" = [(5, 1), (15, 5), (30, 10), (45, 15), (60, 25), (90, 30)]
selected: int = 3


# Code in a 'while True:' loop repeats forever
while True:
    print("INFO: selected timer -> " + str(durations[selected]))
    display.scroll(str(durations[selected]))
    sleep(1000)

    selected = wait_for_pin_logo(selected, durations)

    reset_button_states()

    display.show(Image.YES)

    tomato: Pomodoro = Pomodoro(*durations[selected])

    tomato.start_timer()
