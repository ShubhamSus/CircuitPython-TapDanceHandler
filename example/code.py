import board
from keypad_tapdance import Keyboard

# Define keypad pins
ROWS = (board.GP15, board.GP14, board.GP13)
COLS = (board.GP12, board.GP11, board.GP10, board.GP9)

keyboard  = Keyboard(ROWS, COLS)

try:
    while True:
        keyboard.update()
        
        event = keyboard.get()
        if event:
            print(event)
        
except KeyboardInterrupt as ex:
    print(ex)
