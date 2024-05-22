# Imports go at the top
import music as Music
from microbit import *


class MusicBrowser:
    # Music icon
    LOGO: Image = Image.MUSIC_QUAVERS

    PLAY: Image = Image(
            "00000:"
            "09900:"
            "09090:"
            "09900:"
            "00000:"
    )  # fmt: off

    PAUSE: Image = Image(
            "00000:"
            "09090:"
            "09090:"
            "09090:"
            "00000:"
    )  # fmt: off

    STOP: Image = Image(
            "00000:"
            "09990:"
            "09090:"
            "09990:"
            "00000:"
    )  # fmt: off

    FWD: Image = Image(
            "00000:"
            "90090:"
            "99099:"
            "90090:"
            "00000:"
    )  # fmt: off

    BWD: Image = Image(
            "00000:"
            "09009:"
            "99099:"
            "09009:"
            "00000:"
    )  # fmt: off

    SOUND: Image = Image(
            "00090:"
            "99009:"
            "99009:"
            "99009:"
            "00090:"
    )  # fmt: off

    def __init__(self) -> None:
        """Initialize MusicBrowser."""

        display.show(self.LOGO)
        sleep(1_000)

        self.index: int = 0
        self.songs: "list[str]" = [music for music in dir(Music) if music.isupper()]
        self.song: str = self.songs[self.index]
        self.size: int = len(self.songs)

        print("INFO: songs=" + str(self.songs))

    def browse_left(self) -> None:
        """Scroll carousel to the left."""

        self.index = (self.index - 1) % self.size
        self.song = self.songs[self.index]

        self.show()

    def browse_right(self) -> None:
        """Scroll carousel to the right."""

        self.index = (self.index + 1) % self.size
        self.song = self.songs[self.index]

        self.show()

    def show(self) -> None:
        """Show the current song."""

        print("INFO: song: " + self.song)
        display.scroll(self.song)

    def play(self) -> None:
        """Play the current song."""

        display.show(self.SOUND)
        Music.play(getattr(Music, self.song))


print()
print("Music Browser")
print()

app: MusicBrowser = MusicBrowser()

# Code in a 'while True:' loop repeats forever
while True:
    display.show(app.BWD)
    sleep(500)
    display.show(app.FWD)
    sleep(500)

    app.show()
    sleep(500)

    app.play()
    sleep(500)

    if button_a.was_pressed():
        app.browse_left()
    elif button_b.was_pressed():
        app.browse_right()
