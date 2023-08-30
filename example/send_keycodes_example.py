import board
import usb_hid
from keypad_tapdance import Keeb

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

kbd = Keyboard(usb_hid.devices) # usb_hid Keyboard Object
keymap = {
    0.0:Keycode.A,
    0.1:Keycode.B,
    0.2:Keycode.C,
    #############
    1.0:Keycode.D,
    1.1:Keycode.E,
    1.2:Keycode.F
}

# Define Keypad Pins For Tapdance Handler
ROWS = (board.GP15, board.GP14, board.GP13)
COLS = (board.GP12, board.GP11, board.GP10, board.GP9)
COLUMNS_TO_ANODES = True

keyboard  = Keeb(ROWS, COLS, COLUMNS_TO_ANODES)

try:
    while True:
        keyboard.update()

        events = keyboard.get()
        if events:
            #print(f"<Key {event}>")
            for key in events: # Loop Through All Events If Mulitple Keys Are Pressed At Same Time
                if key in keymap: # Check If Key Exists In KeyMap Dict
                    kbd.send(keymap[key]) # Press And Release The Key
                
except KeyboardInterrupt as ex:
    pass
