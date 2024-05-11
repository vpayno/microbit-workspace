# Imports go at the top
from microbit import *
import log

print("INFO: spining wheel while we log data")
print("INFO: data is in MY_DATA.HTM file")
print("INFO: ok, the interactive log file is pretty cool")

log.set_labels('x', 'y', 'z')

print("INFO: mirroring log to console")
log.set_mirroring(True)

print("INFO: shake the microbit")

@run_every(s=1)
def log_data():
    log.add({
      'x': accelerometer.get_x(),
      'y': accelerometer.get_y(),
      'z': accelerometer.get_z(),
    })


while True:
    display.show(Image.ALL_CLOCKS)
    sleep(1000)
