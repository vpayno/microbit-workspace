# Imports go at the top
from microbit import *


class SoundBrowser:
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
        """Initialize SoundBrowser."""

        display.show(self.LOGO)
        sleep(1_000)

        self.index: int = 0
        self.sounds: "list[str]" = [sound for sound in dir(Sound) if sound.isupper()]
        self.sound: str = self.sounds[self.index]
        self.size: int = len(self.sounds)

        print("INFO: sounds=" + str(self.sounds))

    def browse_left(self) -> None:
        """Scroll carousel to the left."""

        self.index = (self.index - 1) % self.size
        self.sound = self.sounds[self.index]

        self.show()

    def browse_right(self) -> None:
        """Scroll carousel to the right."""

        self.index = (self.index + 1) % self.size
        self.sound = self.sounds[self.index]

        self.show()

    def show(self) -> None:
        """Show the current sound."""

        print("INFO: sound: " + self.sound)
        display.scroll(self.sound)

    def play(self) -> None:
        """Play the current sound."""

        display.show(self.SOUND)
        audio.play(getattr(Sound, self.sound))


print()
print("Sound Browser")
print()

app: SoundBrowser = SoundBrowser()


# Code in a 'while True:' loop repeats forever
while True:
    sleep(1_000)
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
