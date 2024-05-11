# Imports go at the top
from microbit import *

images: "list[str]" = [image for image in dir(Image) if image.isupper()]
index: int = -1
COUNT: int = len(images)

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
        print("INFO: not doing anything since the last image is already in a loop")

    image: str

    if index == -1:
        image = "SAD"
    else:
        image = images[index]

    print("INFO: image: " + image)
    display.scroll(image)
    display.show(getattr(Image, image))

    sleep(1000)
