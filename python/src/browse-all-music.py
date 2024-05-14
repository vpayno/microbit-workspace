# Imports go at the top
import music as Music
from microbit import *

songs: "list[str]" = [music for music in dir(Music) if music.isupper()]
index: int = -1
COUNT: int = len(songs)


def browse_left(index: int) -> int:
    return (index - 1) % COUNT


def browse_right(index: int) -> int:
    return (index + 1) % COUNT


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        index = browse_left(index)
    elif button_b.was_pressed():
        index = browse_right(index)
    elif pin_logo.is_touched():
        print("INFO: not doing anything since the last song is already in a loop")

    song: str

    if index == -1:
        song = "BA_DING"
    else:
        song = songs[index]

    print("INFO: song: " + song)
    display.scroll(song)
    Music.play(getattr(Music, song))

    sleep(1000)
