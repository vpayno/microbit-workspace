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

### Browse All Symbols

Here we go, an image/symbol browser!

- `button_a` scrolls left
- `button_b` scrolls right
- `pin_logo` replays the current image

### Play All Sounds

Needed a way to hear all the pre-defined sounds.

Should add button functionality to manually browse them.

### Browse All Sounds

Here we go, a sound browser!

- `button_a` scrolls left
- `button_b` scrolls right
- `pin_logo` replays the current sound

### Press a Button

The buttons `button_a` and `button_b` have 3 methods:

- `get_presses()`: returns the running total of the press events and resets the counter
- `is_pressed()`: returns true if the button is currently in the pressed position
- `was_pressed()`: returns true if the button was pressed since the last time we checked

### Pet a Microbit

Pet the Microbit by holding the logo button.

- `pin_logo.is_touiched()`: returns true if the logo is currently being touched.

### Sound Meter

Shows the sound level from the microphone from `0` to `255`.

Need to add a graphical graph of the sound levels.

- `microphone.get_events()`: returns a touple of sound events
- `microphone.is_event()`: returns true if the last sound event occurred
- `microphone.set_threshold(SoundEvent, value)`: adjust the sensitivity of the microphone
- `microphone.sound_level()`: returns the sound pressure level from 0 to 255
- `microphone.was_event()`: returns true if a sound event occurred since the last time it was checked

### Light Meter

Uses the LED to measure light.

- `display.read_light_level()`: number from 0 to 255, not very sensitive

### Temperature Meter

Add a graph of the temperature?

- `temperature()`: returns the integer temperature in Celsius

### Fake Compass

Uses an arrow to show which direction it's pointing in.

Not very useful as a compass.

Need a new version that ses animation to show where North, East, West and South always are like a real compass.

- `heading()`: has the annoying habit of forcing recalibrations, returns a number from 0 to 355 representing the degrees from North starting at 0°.

### Real Compass

This version behaves like a real compass.

### Spin the Wheel

Uses buttons instead of the compass to spin the arrow.

### Random Pointer

Uses the random number generator to direct the direction of the arrow.

### Data Logger

This is cool, it creates an interactive data file with the logged data.

- `log.set_mirroring(bool)`: mirrors log data to the console
- `log.set_labels(label1, ...)`: text labels of data
- `log.add(label, function, ...)`: map functions to labels
- `@run_every(seconds)`: decorator used on a custom function to log data in the background

### Shake Logger

Logs the accelerometer's data.

- `accelerometer.get_x()`: returns the acceleration measurement in the x axis in milli-g
- `accelerometer.get_y()`: returns the acceleration measurement in the y axis in milli-g
- `accelerometer.get_z()`: returns the acceleration measurement in the z axis in milli-g

### Dice

Took a sec to get the order of events right so there's a low lag between button presses and user feedback.
Using `button_x.get_presses()` helped a lot with the "responsiveness" feel of the app.

Uses button `a` to decrement the dice face count and button `b` to increment the face count. Valid dice faces/sides are 4, 6, 8, 12 and 20.

The user shakes the `microbit` to use the rng to roll the dice.
If the user shakes it violently, it displays an angry face and rolls the dice anyway.
