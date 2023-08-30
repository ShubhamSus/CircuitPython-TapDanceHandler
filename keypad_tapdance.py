from keypad import KeyMatrix
from adafruit_ticks import ticks_ms, ticks_diff

class KeyState:
    def __init__(self) -> None:
        self.pressed = False
        self.last_change_ms = 0
        self.short_counter = 0
        self.short_show = 0
        self.long_registered = False
        self.long_show = False

class Keeb:
    def __init__(self, row_pins, col_pins, columns_to_anodes:bool = True, short_duration_ms:int = 100, long_duration_ms:int = 600) -> None:
        # Initialize the keypad and set the time durations for short and long presses
        self.keys = KeyMatrix(row_pins=row_pins, column_pins=col_pins, columns_to_anodes=columns_to_anodes)
        
        self.SHORT_DURATION_MS = short_duration_ms
        self.LONG_DURATION_MS = long_duration_ms
        
        self.key_states = [KeyState() for _ in range(self.keys.key_count)]
        self.events = []
        
    def update(self) -> None:
        # Get the latest key events from the keypad
        key_events = self.keys.events.get()
        
        if key_events:
            #key = self.key_events.key_number # Get Current Pressed Key Index
            state = self.key_states[key_events.key_number] # Get Instance Of KeyState Class For Current Key
            
            if key_events.pressed:
                # Update key state for a pressed event
                state.pressed = True
                state.last_change_ms = ticks_ms()  # Record the time of the event
                state.short_counter += 1  # Increment short press counter
                
            elif key_events.released:
                # Update key state for a released event
                state.pressed = False
                state.last_change_ms = ticks_ms()  # Record the time of the event
                if state.long_registered:
                    state.long_registered = False  # Reset long press registration if key is released
        
        self.events = []
        
        for key, state in enumerate(self.key_states):
            # Calculate the time since the last change of key state
            duration = ticks_diff(ticks_ms(), state.last_change_ms)
            
            if not state.long_registered and state.pressed and duration >= self.LONG_DURATION_MS:
                # Register long press if the long duration is reached
                state.long_registered = True
                state.long_show = True
                state.short_counter = 0  # Reset short press counter
            
            elif state.short_counter > 0 and not state.pressed and duration >= self.SHORT_DURATION_MS:
                # Set short_show if the short duration is reached after key release
                state.short_show = state.short_counter 
                state.short_counter = 0  # Reset short press counter
            
            else:
                # Reset the show indicators if conditions are not met
                state.long_show = False
                state.short_show = 0
            
            # Determine the key press type and add it into list of events
            if state.short_show == 1:
                self.add_event(key, 0) # Single Clicked
            elif state.short_show == 2:
                self.add_event(key, 1) # Double Clicked           
            elif state.long_show:
                self.add_event(key, 2) # Long Press
                
    def get(self) -> list:
        return self.events
    
    def add_event(self, keyIndex, eventType) -> None:
        #self.events.append(f"{keyIndex}.{eventType}")
        combined_float = keyIndex + eventType / 10
        self.events.append(combined_float)