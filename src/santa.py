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

        # --- BINDINGS ---
        self.root.bind("<Button-3>", self.quit_app)  # Right Click -> Exit
        
        # New Drag & Drop Bindings
        self.label.bind("<Button-1>", self.start_drag)         # Click
        self.label.bind("<B1-Motion>", self.do_drag)           # Drag
        self.label.bind("<ButtonRelease-1>", self.stop_drag)   # Release

        # 4. Setup Behavior
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
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

    # --- DRAG HANDLERS ---
    def start_drag(self, event):
        # event.x_root is the global screen coordinate of the mouse
        self.brain.start_drag(event.x_root, event.y_root)

    def do_drag(self, event):
        x, y = self.brain.update_drag(event.x_root, event.y_root)
        self.root.geometry(f"+{x}+{y}")

    def stop_drag(self, event):
        self.brain.end_drag()

    # --- UPDATE LOOPS ---
    def update_movement(self):
        current_state = self.brain.state
        
        if current_state == 'WALKING':
            new_x, new_y = self.brain.calculate_next_step(config.SPEED)
            self.root.geometry(f"+{new_x}+{new_y}")
            self.root.after(config.MOVEMENT_DELAY, self.update_movement)
            
        elif current_state == 'FALLING':
            new_x, new_y = self.brain.apply_gravity(config.GRAVITY)
            self.root.geometry(f"+{new_x}+{new_y}")
            # Falling should be faster/smoother than walking
            self.root.after(config.FALL_DELAY, self.update_movement)
            
        elif current_state == 'DRAGGING':
            # While dragging, the mouse event handles the movement
            # We just keep the loop alive
            self.root.after(config.MOVEMENT_DELAY, self.update_movement)

    def update_animation(self):
        frame = self.animator.next_frame()
        if frame:
            self.label.config(image=frame)
        self.root.after(config.ANIMATION_DELAY, self.update_animation)

    def quit_app(self, event):
        self.root.destroy()
        return "break"