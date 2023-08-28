from keypad import KeyMatrix
from adafruit_ticks import ticks_ms, ticks_diff

class KeyState:
    def __init__(self):
        self.pressed = False
        self.last_change_ms = 0
        self.short_counter = 0
        self.short_show = 0
        self.long_registered = False
        self.long_show = False
        

class Keyboard:
    def __init__(self, row_pins, col_pins, short_duration_ms: int = 90, long_duration_ms: int = 450):
        # Initialize the keypad and set the time durations for short and long presses
        self.keys = KeyMatrix(row_pins=row_pins, column_pins=col_pins, columns_to_anodes=True)
        self.short_duration_ms = short_duration_ms
        self.long_duration_ms = long_duration_ms
        self.key_states = [KeyState() for _ in range(self.keys.key_count)]
        
        self.events = []
        
    def update(self):
        # Get the latest key events from the keypad
        self.key_events = self.keys.events.get()
        if self.key_events:
            key = self.key_events.key_number # Get Current Pressed Key Index
            state = self.key_states[key] # Get Instance Of KeyState Class For Current Key
            
            if self.key_events.pressed:
                # Update key state for a pressed event
                state.pressed = True
                state.last_change_ms = ticks_ms()  # Record the time of the event
                state.short_counter += 1  # Increment short press counter
                
            elif self.key_events.released:
                # Update key state for a released event
                state.pressed = False
                state.last_change_ms = ticks_ms()  # Record the time of the event
                if state.long_registered:
                    state.long_registered = False  # Reset long press registration
        
        self.events = []
        for key, state in enumerate(self.key_states):
            # Calculate the time since the last change of key state
            duration = ticks_diff(ticks_ms(), state.last_change_ms)
            
            if not state.long_registered and state.pressed and duration > self.long_duration_ms:
                # Register long press if the long duration is reached
                state.long_registered = True
                state.long_show = True
                state.short_counter = 0  # Reset short press counter
            
            elif state.short_counter > 0 and not state.pressed and duration > self.short_duration_ms:
                # Set short_show if the short duration is reached after key release
                state.short_show = state.short_counter
                state.short_counter = 0  # Reset short press counter
            
            else:
                # Reset the show indicators if conditions are not met
                state.long_show = False
                state.short_show = 0
            
            # Determine the key press type and return the corresponding message
            if state.short_show == 1:
                #return f"{key}.{0} Single Clicked"
                self.events.append(f"{key}.{0}")
            elif state.short_show == 2:
                #return f"{key}.{1} Double Clicked"
                self.events.append(f"{key}.{1}")           
            elif state.long_show:
                #return f"{key}.{2} Long Pressed"
                self.events.append(f"{key}.{2}")
                
    def get(self) -> list:
        return self.events
    
    def short_press(self, key_index) -> int:
        return self.key_states[key_index].short_show
    
    def long_press(self, key_index) -> bool:
        return self.key_states[key_index].long_show
