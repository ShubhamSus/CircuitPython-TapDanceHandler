import board
import usb_hid
from keypad_tapdance import Keeb

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

# Define keypad pins
ROWS = (board.GP15, board.GP14, board.GP13)
COLS = (board.GP12, board.GP11, board.GP10, board.GP9)
COLUMNS_TO_ANODES = True

keyboard  = Keeb(ROWS, COLS, COLUMNS_TO_ANODES)


kbd = Keyboard(usb_hid.devices)
keymap = {
    0.0:Keycode.A,
    0.1:Keycode.B,
    0.2:Keycode.C,
    #############
    1.0:Keycode.D,
    1.1:Keycode.E,
    1.2:Keycode.F
}


try:
    while True:
        keyboard.update()

        event = keyboard.get()
        if event:
            #print(f"<Key {event}>")
            for key in event:
                kbd.send(keymap[float(key)])
                
        
except KeyboardInterrupt as ex:
    print(ex)
