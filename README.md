
Introduction
============
Simple CircuitPython Library for Keypad/KeyMatrix TapDance Functionality.




## Dependencies

- [CircuitPython KeyMap](https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html)
## Usage/Examples

```python
import board
from keypad_tapdance import Keyboard

# Define keypad pins
ROWS = (board.GP15, board.GP14, board.GP13)
COLS = (board.GP12, board.GP11, board.GP10, board.GP9)

keyboard  = Keyboard(ROWS, COLS)

try:
    while True:
        key = keyboard.update()
        if key != None:
            print(key)
        
except KeyboardInterrupt as ex:
    print(ex)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

