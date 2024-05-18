# Imports go at the top
from microbit import *
import music
from math import ceil
import log

# Pomodoro Timer Class
class Pomodoro():
    def __init__(self, log_mode_enabled: bool, work_duration: int = 45, break_duration: int = 15) -> None:
        """
        :param work_duration: the length, in minutes, of the work timer
        :param break_duration: the length, in minutes, of the break timer
        """

        self.name = "generic"
        self.seconds_in_minute: int = 60
        self.time_left: int = 0
        self.work_duration: int = work_duration
        self.break_duration: int = break_duration
        self.second: int = 1_000
        self.warned: bool = False
        self.completed: bool = False
        self.log_enabled: bool = log_mode_enabled

    def _log_data(self) -> None:
        """Logs data on demand."""
        if self.log_enabled:
            # print("LOG: name=" + self.name + ", duration=" + str(getattr(self, self.name + "_duration")) + ", completed=" + str(self.completed))
            log.add({
              'name': self.name,
              'duration': getattr(self, self.name + "_duration"),
              'completed': str(self.completed)
            })

    def _five_minute_warning(self, fives_left: int) -> None:
        """Private method used to issue the five minute warnings.

        :param fives_left: the number of 5 minute chunks left in the running timer.
        """

        if self.time_left == 1 and (self.work_duration == 5 or self.break_duration == 5):
            print("INFO: 1 minute warning at " + str(self.time_left) + " minutes")
            play_music_warning("BADDY")
        elif fives_left == 1 and not self.warned and (self.work_duration > 5 or self.break_duration > 5):
            print("INFO: 5 minute warning at " + str(self.time_left) + " minutes")
            play_music_warning("BADDY")

            if self.time_left == 5:
                print("INFO: disabling timer warnings")
                self.warned = not self.warned


    def _run_timer(self, name: str, duration: int) -> bool:
        """ Runs the internal timer

        :param name: work or break
        :param duration: in minutes
        :return: true, completed | false, canceled
        """

        print("INFO: starting " + name + " timer for " + str(duration) + " minutes")
        print("INFO: logging enabled? " + "yes" if self.log_enabled else "no")

        self.name = name

        display.scroll(str(duration))

        self.time_left = duration

        while self.time_left > 0:
            print("INFO: " + str(self.time_left) + " minutes left in " + name + " timer")

            # there are 12 fives in an hour, we can use that to
            # show timer progress in a non-distracting way
            fives: int = int(ceil((self.time_left % 60) / 5))
            if fives == 0:
                fives = 12
            clock_name: str = "CLOCK" + str(fives)

            print("INFO: showing clock face -> " + clock_name)
            display.show(getattr(Image, clock_name))

            self._five_minute_warning(fives)

            self.time_left -= 1

            heartbeat: bool = True
            count: int = self.seconds_in_minute

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
                        sleep(1_000)

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

        self.completed = self._run_timer("work", self.work_duration)

        if self.completed:
            self._log_data()
            print("INFO: work timer completed")
            display.show(Image.HAPPY)
            play_sound_warning("HAPPY")
            sleep(1_000)

            print("==============================")

            self.completed = False
            self.warned = False

            self.completed = self._run_timer("break", self.break_duration)

            if self.completed:
                self._log_data()
                print("INFO: break timer completed")
                display.show(Image.FABULOUS)
                play_sound_warning("HAPPY")
                sleep(1_000)
            else:
                self._log_data()
                print("INFO: break timer canceled")

        else:
            self._log_data()
            print("INFO: work timer canceled")


# Helper functions

def play_sound_warning(sound: str) -> None:
    print("INFO: playing Sound." + sound)
    audio.play(getattr(Sound, sound))


def play_music_warning(song: str) -> None:
    print("INFO: playing music." + song)
    music.play(getattr(music, song))


def reset_button_states() -> None:
    """We need to read buttons again after reading them to make sure
    that users can't stack button presses."""

    _ = button_a.was_pressed()
    _ = button_b.was_pressed()


def wait_for_pin_logo(log_mode_enabled: bool, selected: int, durations: "list[tuple[int, int]]") -> "tuple[int, bool]":
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
        display.show(Image.ARROW_E)
        sleep(500)

        # sleep(1_000)
        # display.show(Image.ALL_ARROWS)

        if button_a.was_pressed():
            reset_button_states()
            selected = (selected + 1) % len(durations)

            print("INFO: selected timer -> " + str(durations[selected]))
            display.scroll(str(durations[selected]))
            sleep(500)

            display.show(Image.ARROW_N)

        if button_b.was_pressed():
            reset_button_states()
            log_mode_enabled = not log_mode_enabled
            print("INFO: logging enabled? " + "yes" if log_mode_enabled else "no")
            display.scroll("log:" + str(log_mode_enabled))
            sleep(500)

    return (selected, log_mode_enabled)


# defaults to 45:15
durations: "list[tuple[int, int]]" = [(5, 1), (15, 5), (30, 10), (45, 15), (60, 25), (90, 30)]
selected: int = 3
log_mode_enabled: bool = False
log.set_mirroring(True)
log.set_labels("name", "duration", "completed", timestamp=log.SECONDS)

# trying to increase the likelihood that the startup output doesn't get discarded
sleep(100)
print()
print("START: Pomodoro Timer")
print()

# Code in a 'while True:' loop repeats forever
while True:
    print("INFO: selected timer -> " + str(durations[selected]))
    display.scroll(str(durations[selected]))
    sleep(1_000)

    selected, log_mode_enabled = wait_for_pin_logo(log_mode_enabled, selected, durations)

    reset_button_states()

    display.show(Image.YES)

    tomato: Pomodoro = Pomodoro(log_mode_enabled, *durations[selected])

    tomato.start_timer()
