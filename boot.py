import board
from digitalio import DigitalInOut, Direction, Pull
import time
import storage

btn = DigitalInOut(board.GP24)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

time.sleep(0.2)

if not btn.value:
    storage.enable_usb_drive()
    print("USB Storage enabled")
else:
    storage.disable_usb_drive()
    print("USB Storage disabled")