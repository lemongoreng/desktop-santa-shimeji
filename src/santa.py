import tkinter as tk
import config
from animation import GifAnimator
from behavior import SantaBehavior

class DesktopSanta:
    def __init__(self, root):
        self.root = root

        # 1. Setup Window
        self.setup_window()

        # 2. Load Assets
        asset_path = config.get_asset_path('santa.gif')
        self.animator = GifAnimator(asset_path)
        
        # 3. Setup Label
        first_frame = self.animator.get_first_frame()
        self.label = tk.Label(self.root, image=first_frame, bg='black', bd=0)
        self.label.pack()
        self.root.bind("<Button-3>", self.quit_app)

        # 4. Setup Behavior (The Brain)
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        # Calculate floor Y position based on image height
        santa_h = first_frame.height()
        floor_y = screen_h - santa_h - config.BOTTOM_OFFSET
        
        self.brain = SantaBehavior(screen_w, floor_y)

        # 5. Start Loops
        self.update_movement()
        self.update_animation()

    def setup_window(self):
        self.root.overrideredirect(True)
        self.root.config(bg='black')
        self.root.wm_attributes("-transparentcolor", "black")
        self.root.wm_attributes("-topmost", True)

    def update_movement(self):
        # Ask the brain for the next coordinates
        new_x, new_y = self.brain.calculate_next_step(config.SPEED)
        
        # Update Window Position
        w = self.animator.get_first_frame().width()
        h = self.animator.get_first_frame().height()
        self.root.geometry(f'{w}x{h}+{new_x}+{new_y}')
        
        # Loop
        self.root.after(config.MOVEMENT_DELAY, self.update_movement)

    def update_animation(self):
        # Get next frame from animator
        frame = self.animator.next_frame()
        if frame:
            self.label.config(image=frame)
        
        # Loop
        self.root.after(config.ANIMATION_DELAY, self.update_animation)

    def quit_app(self, event):
        self.root.destroy()
        return "break"