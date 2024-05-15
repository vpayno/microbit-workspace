# Imports go at the top
from microbit import *

sounds: "list[str]" = [sound for sound in dir(Sound) if sound.isupper()]
index: int = -1
COUNT: int = len(sounds)


def browse_left(index: int) -> int:
    """Scroll carousel to the left.

    :param index: the current position
    :return: the new position
    """
    return (index - 1) % COUNT


def browse_right(index: int) -> int:
    """Scroll carousel to the right.

    :param index: the current position
    :return: the new position
    """
    return (index + 1) % COUNT


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.ARROW_E)
    sleep(500)
    display.show(Image.ARROW_W)
    sleep(500)

    if button_a.was_pressed():
        index = browse_left(index)
    elif button_b.was_pressed():
        index = browse_right(index)

    sound: str

    if index == -1:
        sound = "SAD"
    else:
        sound = sounds[index]

    print("INFO: sound: " + sound)
    display.scroll(sound)
    audio.play(getattr(Sound, sound))

    sleep(1000)
