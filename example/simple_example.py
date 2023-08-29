import board
from keypad_tapdance import Keeb

# Define keypad pins
ROWS = (board.GP15, board.GP14, board.GP13)
COLS = (board.GP12, board.GP11, board.GP10, board.GP9)
COLUMNS_TO_ANODES = True

keyboard  = Keeb(ROWS, COLS, COLUMNS_TO_ANODES)

try:
    while True:
        keyboard.update()
        
        event = keyboard.get()
        if event:
            print(f"<Key {event}>")
        
except KeyboardInterrupt as ex:
    print(ex)
