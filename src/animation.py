import tkinter as tk
from config import SCALE_FACTOR

class GifAnimator:
    def __init__(self, asset_map):
        # asset_map is a dictionary: {'WALKING': path_to_walk, 'FALLING': path_to_fall...}
        self.animations = {}
        self.current_state = None
        self.frames = []
        self.current_index = 0
        
        # Load ALL animations into memory
        for state, path in asset_map.items():
            self.load_animation(state, path)

    def load_animation(self, state, path):
        loaded_frames = []
        index = 0
        while True:
            try:
                frame = tk.PhotoImage(file=path, format=f'gif -index {index}')
                frame = frame.subsample(SCALE_FACTOR)
                loaded_frames.append(frame)
                index += 1
            except tk.TclError:
                break
        if loaded_frames:
            self.animations[state] = loaded_frames
            print(f"Loaded {state}: {len(loaded_frames)} frames")
        else:
            print(f"Warning: No frames found for {state} at {path}")

    def set_state(self, new_state):
        # Only switch if the state is actually different
        if self.current_state != new_state and new_state in self.animations:
            self.current_state = new_state
            self.frames = self.animations[new_state]
            self.current_index = 0

    def next_frame(self):
        if not self.frames:
            return None
        
        self.current_index += 1
        if self.current_index >= len(self.frames):
            self.current_index = 0
            
        return self.frames[self.current_index]

    def get_current_frame(self):
        return self.frames[self.current_index] if self.frames else None