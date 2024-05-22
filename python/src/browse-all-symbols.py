# Imports go at the top
from microbit import *


class ImageBrowser:
    LOGO: Image = Image.HAPPY

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

    def __init__(self) -> None:
        """Initialize ."""

        display.show(self.LOGO)
        sleep(1_000)

        self.index: int = 0
        self.images: "list[str]" = [image for image in dir(Image) if image.isupper()]
        self.image: str = self.images[self.index]
        self.size: int = len(self.images)

        print("INFO: images=" + str(self.images))

    def browse_left(self) -> None:
        """Scroll carousel to the left."""

        self.index = (self.index - 1) % self.size
        self.image = self.images[self.index]

        self.show()

    def browse_right(self) -> None:
        """Scroll carousel to the right."""

        self.index = (self.index + 1) % self.size
        self.image = self.images[self.index]

        self.show()

    def show(self) -> None:
        """Show the current image."""

        print("INFO: image: " + self.image)
        display.scroll(self.image)

    def play(self) -> None:
        """Play the current image."""

        display.show(getattr(Image, self.image))


print()
print("Image Browser")
print()

app: ImageBrowser = ImageBrowser()


# Code in a 'while True:' loop repeats forever
while True:
    display.show(app.BWD)
    sleep(500)
    display.show(app.FWD)
    sleep(500)

    app.show()
    sleep(500)

    app.play()
    sleep(1_000)

    if button_a.was_pressed():
        app.browse_left()
    elif button_b.was_pressed():
        app.browse_right()
