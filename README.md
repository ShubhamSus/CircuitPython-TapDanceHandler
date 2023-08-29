# Overview
Simple CircuitPython Library for TapDance Functionality using Keypad/KeyMatrix.

## Dependencies

- [CircuitPython KeyMap](https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html)
- [Adafruit Ticks](https://docs.circuitpython.org/projects/ticks/en/latest/api.html)
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
        keyboard.update()
        
        event = keyboard.get()
        if event:
            print(f"<Key {event}>")
        
except KeyboardInterrupt as ex:
    print(ex)
```

To implement multi-click detection in the `keypad_tapdance.py` script based on the desired number of clicks, you can use the following revised code snippet:
```python
# Determine the key press type and return the corresponding message
if state.short_show == 1:
    #return f"{key}.{0} Single Clicked"
    self.events.append(f"{key}.{0}")
elif state.short_show == 2:
    #return f"{key}.{1} Double Clicked"
    self.events.append(f"{key}.{1}")
elif state.short_show == 3:
    #return f"{key}.{1} Triple Clicked"
    self.events.append(f"{key}.{2}")           
elif state.long_show:
    #return f"{key}.{2} Long Pressed"
    self.events.append(f"{key}.{3}")
```
## License

[MIT](LICENSE)

