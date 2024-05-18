# Imports go at the top
import music as Music
from microbit import *

songs: "list[str]" = [music for music in dir(Music) if music.isupper()]
index: int = -1
COUNT: int = len(songs)


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

    song: str

    if index == -1:
        song = "BA_DING"
    else:
        song = songs[index]

    print("INFO: song: " + song)
    display.scroll(song)
    Music.play(getattr(Music, song))

    sleep(1_000)
