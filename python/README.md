# microbit python experiments

Journaling Microbit MicroPython experiments here.

Not too impressed with the command line tools.

Going to stick to the [online editor](https://python.microbit.org/v/3) for now.

## Experiments

Using the [online editor](https://python.microbit.org/v/3) to test these.

I need to spend more time learning how to use the command-line tools.

### Hello World

Unicode characters only seem to work in the console.
The Dot display shows `?` for every byte.

- `display.scroll(text)`: uses a scroll animation to display all the characters in the string
- `display.show(text)`: shows one character at a time without any animation
- `audio.play(Sound)`: plays a sound
- `speech.say(text)`: it just seems to play jiberish

### Show All Symbols

Needed a way to see all the pre-defined symbols.

Should add button functionality to manually browse them.

### Play All Sounds

Needed a way to hear all the pre-defined sounds.

Should add button functionality to manually browse them.

### Press a Button

The buttons `button_a` and `button_b` have 3 methods:

- `get_presses()`: returns the running total of the press events and resets the counter
- `is_pressed()`: returns true if the button is currently in the pressed position
- `was_pressed()`: returns true if the button was pressed since the last time we checked

### Pet a Microbit

Pet the Microbit by holding the logo button.

- `pin_logo.is_touiched()`: returns true if the logo is currently being touched.
