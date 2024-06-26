# microbit python experiments

Journaling Microbit MicroPython experiments here.

Not too impressed with the command line tools.

Going to stick to the [online editor](https://python.microbit.org/v/3) for now.

## Experiments

Using the [online editor](https://python.microbit.org/v/3) to test these.

I need to spend more time learning how to use the command-line tools.

### [Hello World](./src/hello-world.py)

Unicode characters only seem to work in the console.
The Dot display shows `?` for every byte.

- `display.scroll(text)`: uses a scroll animation to display all the characters in the string
- `display.show(text)`: shows one character at a time without any animation
- `audio.play(Sound)`: plays a sound
- `speech.say(text)`: it just seems to play gibberish

### [Show All Symbols](./src/show-all-symbols.py)

Needed a way to see all the pre-defined symbols.

Should add button functionality to manually browse them.

### [Browse All Symbols](./src/browse-all-symbols.py)

Here we go, an image/symbol browser!

- `button_a` scrolls left
- `button_b` scrolls right
- `pin_logo` replays the current image

### [Play All Sounds](./src/play-all-sounds.py)

Needed a way to hear all the pre-defined sounds.

Should add button functionality to manually browse them.

### [Browse All Sounds](./src/browse-all-sounds.py)

Here we go, a sound browser!

- `button_a` scrolls left
- `button_b` scrolls right
- `pin_logo` replays the current sound

### [Browse All Music](./src/browse-all-music.py)

Here we go, a music browser!

- `button_a` scrolls left
- `button_b` scrolls right
- `pin_logo` replays the current sound

### [Press a Button](./src/press-a-button.py)

The buttons `button_a` and `button_b` have 3 methods:

- `get_presses()`: returns the running total of the press events and resets the counter
- `is_pressed()`: returns true if the button is currently in the pressed position
- `was_pressed()`: returns true if the button was pressed since the last time we checked

### [Pet a Microbit](./src/pet-the-microbit.py)

Pet the Microbit by holding the logo button.

- `pin_logo.is_touiched()`: returns true if the logo is currently being touched.

### [Sound Meter](./src/sound-meter.py)

Shows the sound level from the microphone from `0` to `255`.

Need to add a graphical graph of the sound levels.

- `microphone.get_events()`: returns a tuple of sound events
- `microphone.is_event()`: returns true if the last sound event occurred
- `microphone.set_threshold(SoundEvent, value)`: adjust the sensitivity of the microphone
- `microphone.sound_level()`: returns the sound pressure level from 0 to 255
- `microphone.was_event()`: returns true if a sound event occurred since the last time it was checked

### [Light Meter](./src/light-meter.py)

Uses the LED to measure light.

- `display.read_light_level()`: number from 0 to 255, not very sensitive

### [Temperature Meter](./src/temperature-meter.py)

Add a graph of the temperature?

- `temperature()`: returns the integer temperature in Celsius

### [Fake Compass](./src/compass-fake.py)

Uses an arrow to show which direction it's pointing in.

Not very useful as a compass.

Need a new version that uses animation to show where North, East, West and South always are like a real compass.

- `heading()`: has the annoying habit of forcing re-calibrations, returns a number from 0 to 355 representing the degrees from North starting at 0°.

### [Real Compass](./src/compass-real.py)

This version behaves like a real compass.

### [Spin the Wheel](./src/spin-the-wheel.py)

Uses buttons instead of the compass to spin the arrow.

### [Random Pointer](./src/random-pointer.py)

Uses the random number generator to direct the direction of the arrow.

### [Data Logger](./src/data-logger.py)

This is cool, it creates an interactive data file with the logged data.

Example data file: [MY_DATA.HTM](./data/data-logger.htm)

- `log.set_mirroring(bool)`: mirrors log data to the console
- `log.set_labels(label1, ...)`: text labels of data
- `log.add(label, function, ...)`: map functions to labels
- `@run_every(seconds)`: decorator used on a custom function to log data in the background

### [Shake Logger](./src/shake-logger.py)

Logs the accelerometer's data.

- `accelerometer.get_x()`: returns the acceleration measurement in the x axis in milli-g
- `accelerometer.get_y()`: returns the acceleration measurement in the y axis in milli-g
- `accelerometer.get_z()`: returns the acceleration measurement in the z axis in milli-g

### [Dice](./src/dice.py)

Took a sec to get the order of events right so there's a low lag between button presses and user feedback.
Using `button_x.get_presses()` helped a lot with the "responsiveness" feel of the app.

Uses button `a` to decrement the dice face count and button `b` to increment the face count. Valid dice faces/sides are 4, 6, 8, 12 and 20.

The user shakes the `microbit` to use the RNG to roll the dice.
If the user shakes it violently, it displays an angry face and rolls the dice anyway.

### [Entropy meter](./src/entropy-meter.py)

Using the accelerometer to fill in the dots.

It's interesting to just let it sit there and fill in on it's own over time.

### [Game of Life](./src/game-of-life.py)

Trying out implementing the Game of Life on the microbit.

Life is hard on the LEDs.

### [Pomodoro Timer](./src/pomodoro-timer.py)

Simple pomodoro timer.

Example data file: [MY_DATA.HTM](./data/pomodoro-timer.htm)

- defaults to a 45 minute work timer followed by a 15 minute break timer
- issues an audible 5 minute warning
- issues the work/break session end

While in the `up arrow` state (waiting for the user to touch the `pin_logo` button):

- `button_a` scrolls between predefined timers: 45|15, 60|25, 90|30, 5|1, 15|5, 30|10
- `button_b` toggles logging mode, defaults to disabled

After the user presses the `pin_logo` button:

- `button_b` pauses timer and `button_a` unpauses timer
- `button_a` cancels/resets timer

After both the work and break timers complete, it returns to the first state.

### [Random Timer](./src/random-timer.py)

I wanted to implement a timer that used an hourglass animation.
The duration, in seconds, of the timer is set using an RNG.

### [Timer](./src/timer.py)

This is a "normal" timer.

stage1:

- `button_a`: used to select between units of `seconds`, `minutes`, or `hours`
- `button_b`: used to confirm the selection

stage2:

- `pin_logo`: used to select the duration increment number (1, 5, 10, 30, 45)
- `button_a`: used to increment the duration from 0 to the limit for the units:
    - `seconds`: 90 seconds
    - `minutes`: 90 minutes
    - `hours`: 24 hours (batteries don't last that long so good luck with that)
- `button_b`: used to confirm the selection

stage3:

A right arrow points to `button_b` to tell the user how to start the timer.

The timer can also be reset by pressing `button_a`.

stage4:

This is the timer phase. It uses a classic | / - \ wheel animation as the heartbeat.
The pomodoro timer has a way fancier animation.

At `10%` left, it will play `BA_DING` and at completion it will play `DADADADUM`
and show the happy face wearing sunglasses.

- `button_a`: cancels timer, should be ignored during pause
- `button_b`: pauses and unpauses the timer

## [Messenger](./src/messenger.py)

Simple emoji messenger.

stage1: radio group selection

- `button_a`: scroll backward between `0` and `255` by decrements of 7.
- `button_b`: scroll forward between `0` and `255` by increments of 7.
- `pin_logo`: confirms radio group selection.

stage2: emoji selection

- `button_a`: scroll backward emoji list
- `button_b`: scroll forward emoji list
- `pin_logo`: confirms emoji selection.

stage3: both microbits loop sending and receiving until they receive the other's message

- `button_a` or `button_b` will unpause and return to the emoji browser.

## [Rock-Paper-Scissors](./src/rock-paper-scissors.py)

Rock-Paper-Scissors game.

stage1: radio group selection

- `button_a`: scroll backward between `0` and `255` by decrements of 7.
- `button_b`: scroll forward between `0` and `255` by increments of 7.
- `pin_logo`: confirms radio group selection.

stage2: rock-paper-scissor move selection

- `button_a`: scroll backward `[R, P, S]`
- `button_b`: scroll forward `[R, P, S]`
- `pin_logo`: confirms move selection.

stage3: both microbits loop sending and receiving until they receive the other's "move".

- `button_a` or `button_b` will unpause and return to the move selection stage.

## [High Card](./src/high-card.py)

Simple two player high card game.
Each player gets a random number from 0 to 9, inclusive, and then exchange them to see who won.

stage1: radio group selection

- `button_a`: scroll backward between `0` and `255` by decrements of 7.
- `button_b`: scroll forward between `0` and `255` by increments of 7.
- `pin_logo`: confirms radio group selection.

stage2: card selection - replaced with RNG

- `button_a`: scroll backward `[0..9]`
- `button_b`: scroll forward `[0..9]`
- `pin_logo`: confirms move selection.

stage3: both microbits loop sending and receiving until they receive the other's "card".
