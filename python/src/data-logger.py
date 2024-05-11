# Imports go at the top
from microbit import *
import log

print("INFO: spining wheel while we log data")
print("INFO: data is in MY_DATA.HTM file")
print("INFO: ok, the interactive log file is pretty cool")

log.set_labels('temperature', 'sound', 'light')

print("INFO: mirroring log to console")
log.set_mirroring(True)


@run_every(s=5)
def log_data():
    log.add({
      'temperature': temperature(),
      'sound': microphone.sound_level(),
      'light': display.read_light_level()
    })


while True:
    display.show(Image.ALL_CLOCKS)
    sleep(1000)
