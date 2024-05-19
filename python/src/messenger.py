# Imports go at the top

import music
import radio
from microbit import *


class Wheel:
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
        self.wheel_index = (self.wheel_index + 1) % len(self.wheels)
        return self.wheels[self.wheel_index]


class Icons:
    ARROW_UP: Image = Image.ARROW_N
    ARROW_RT: Image = Image.ARROW_E
    ARROW_LT: Image = Image.ARROW_W
    ARROW_DN: Image = Image.ARROW_S

    # signal bars
    LOGO1: Image = Image(
        "00009:"
        "00089:"
        "00789:"
        "06789:"
        "56789:"
    )  # fmt: off

    # square radio waves?
    LOGO2: Image = Image(
        "99999:"
        "96669:"
        "96969:"
        "96669:"
        "99999:"
    )  # fmt: off

    # though bubble
    LOGO3: Image = Image(
        "09990:"
        "90009:"
        "09990:"
        "00900:"
        "00090:"
    )  # fmt: off

    # double horizontal arrow
    LT_RT_ARROW: Image = Image(
        "00900:"
        "09090:"
        "99999:"
        "09090:"
        "00900:"
    )  # fmt: off


class Messenger:
    """Uses the radio to text images."""

    images: "list[str]" = [
        name
        for name in dir(Image)
        if name.isupper() and not (name.startswith("ALL_") or name.startswith("ARROW") or name.startswith("CLOCK"))
    ]

    def __init__(self) -> None:
        """Setup the initial state but don't enable the radio."""

        # prime_numbers: "list[int]" = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]

        self.group: int = -1
        self.group_size: int = 256
        self.group_offset: int = 8  # random.choice(prime_numbers)

        self.power_max: int = 7

        print("INFO: selected prime [" + str(self.group_offset) + "]")

        self.image_index: int = -1
        self.images_size: int = len(self.images)
        self.image_name: str = "None"

        print("INFO: images=" + str(self.images) + "] (" + str(self.images_size) + ")")

    def setup(self) -> None:
        """Enable radio, select group and message."""

        radio.on()
        print("INFO: enabled radio")

        self.group_browse()
        self.image_browse()

    def run(self) -> None:
        """Runs the send/receive loop.

        :return: received message
        """

        response: "str | None" = "None"

        print("INFO: starting send/receive loop")

        wheel: Wheel = Wheel()

        while response == "None" or response is None:
            display.show(wheel.turn())
            radio.send(self.message)
            sleep(500)
            response = radio.receive()
            print("INFO: tentative response [" + str(response) + "]")
            sleep(500)

        self.response: str = str(response)
        print("INFO: accepted response [" + self.response + "]")

    def group_browse(self) -> None:
        """Helps the user select the 'radio frequency'."""

        display.scroll("group")
        sleep(500)

        selected_group: bool = False

        while not selected_group:
            display.show(Image.ARROW_E)
            sleep(500)
            display.show(self.group if self.group in range(0, self.group_size) else "G")
            sleep(500)
            display.show(Image.ARROW_W)
            sleep(500)

            if button_b.was_pressed():
                self.group = (max(self.group, 0) + self.group_offset) % self.group_size
                print("INFO: current group [" + str(self.group) + "]")
                display.scroll(self.group)

            if button_a.was_pressed():
                self.group = (max(self.group, 0) - self.group_offset) % self.group_size
                print("INFO: current group [" + str(self.group) + "]")
                display.scroll(self.group)

            if pin_logo.is_touched() and self.group >= 0:
                selected_group = True
                display.show(Image.YES)
                sleep(1_000)

        print("INFO: selected group [" + str(self.group) + "]")
        display.scroll("g:" + str(self.group))

        print("INFO: config group [" + str(self.group) + "]")
        print("INFO: config power [" + str(self.power_max) + "]")
        radio.config(group=self.group, power=self.power_max)

        sleep(1_000)

    def image_browse(self) -> None:
        """Browe available images to send as a message."""

        display.scroll("image")
        sleep(500)

        self.image_index: int = -1
        self.image_name: str = ""

        selected_image: bool = False

        while not selected_image:
            display.show(Image.ARROW_E)
            sleep(500)
            display.show(self.image_name if self.image_name in self.images else "I")
            sleep(500)
            display.show(Image.ARROW_W)
            sleep(500)

            if button_b.was_pressed():
                self.image_index = (max(self.image_index, 0) + 1) % self.images_size
                self.image_name = self.images[self.image_index]
                print("INFO: current image [" + self.image_name + "]")
                display.scroll(self.images[self.image_index])

            if button_a.was_pressed():
                self.image_index = (max(self.image_index, 0) - 1) % self.images_size
                self.image_name = self.images[self.image_index]
                print("INFO: current image [" + self.image_name + "]")
                display.scroll(self.image_name)

            if pin_logo.is_touched() and self.image_index >= 0:
                selected_image = True
                display.show(Image.YES)
                sleep(1_000)

        print("INFO: selected image [" + self.image_name + "]")
        display.scroll("i:" + self.image_name)
        sleep(1_000)

        self.message: str = self.image_name

    def read_response(self) -> None:
        """Converts str message to an Image."""

        response_text: str = self.response

        print("INFO: response [" + response_text + "]")
        display.show(getattr(Image, response_text))
        music.play(music.BA_DING)
        sleep(5_000)


def reset_button_events() -> None:
    _ = button_a.was_pressed()
    _ = button_b.was_pressed()


def wait_on_any_button() -> None:
    print("INFO: Waiting on any-key press")
    reset_button_events()
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1_000)
    reset_button_events()
    print("INFO: any-key pressed")


print()
print("Radio Messenger")
print()

icons = Icons()
display.show(icons.LOGO3)
sleep(2_000)

app: Messenger = Messenger()
app.setup()

# Code in a 'while True:' loop repeats forever
while True:
    app.run()

    app.read_response()

    wait_on_any_button()

    app.image_browse()
