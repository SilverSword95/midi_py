import adafruit_matrixkeypad
import board
import adafruit_midi
import usb_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from digitalio import DigitalInOut

cols = [DigitalInOut(x) for x in (board.GP7, board.GP10, board.GP11, board.GP12, board.GP13, board.GP8, board.GP14, board.GP15)]
rows = [DigitalInOut(x) for x in (board.GP16, board.GP17, board.GP22, board.GP18, board.GP19, board.GP20, board.GP21)]
keys = ((36,37,38,39,40,41,42,43),(44,45,46,47,48,49,50,51),(52,53,54,55,56,57,58,59),(60,61,62,63,64,65,66,67),(68,69,70,71,72,73,74,75),(76,77,78,79,80,81,82,83),(84,85,86,87,88,89,90,91))
c = 0
pkey = []
for i in range(56):
    pkey.append(0)

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    key = keypad.pressed_keys
    if key:
        for i in range(len(key)):
            if key[i]!=0 and pkey[i]==0:
                midi.send(NoteOn(key[i]))
                pkey[i]=1
            if key[i]==0 and pkey[i]==1:
                midi.send(NoteOff(i+36))
                pkey[i]=0