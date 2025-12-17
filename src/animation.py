import tkinter as tk
from config import SCALE_FACTOR

class GifAnimator:
    def __init__(self, image_path):
        self.frames = []
        self.current_index = 0
        self.load_frames(image_path)

    def load_frames(self, path):
        index = 0
        while True:
            try:
                # Load and Resize
                frame = tk.PhotoImage(file=path, format=f'gif -index {index}')
                frame = frame.subsample(SCALE_FACTOR)
                self.frames.append(frame)
                index += 1
            except tk.TclError:
                break
        
        if not self.frames:
            print(f"Error: No frames loaded from {path}")

    def next_frame(self):
        if not self.frames:
            return None
        
        self.current_index += 1
        if self.current_index >= len(self.frames):
            self.current_index = 0
            
        return self.frames[self.current_index]

    def get_first_frame(self):
        return self.frames[0] if self.frames else None