import tkinter as tk
import config
from animation import GifAnimator
from behavior import SantaBehavior

class DesktopSanta:
    def __init__(self, root):
        self.root = root
        self.setup_window()

        # --- LOAD ASSETS ---
        # Note: If you are missing 'fall.gif', just use 'walk_right.gif' as a placeholder
        assets = {
            'WALK_LEFT':  config.get_asset_path('walk_left.gif'),
            'WALK_RIGHT': config.get_asset_path('walk_right.gif'),
            'FALLING':    config.get_asset_path('falling.gif'),     
            'IDLE':       config.get_asset_path('idle.gif'),     
            'DRAGGING':   config.get_asset_path('dragging.gif')      
        }
        
        self.animator = GifAnimator(assets)
        self.animator.set_state('IDLE')

        # Setup Label
        first_frame = self.animator.get_current_frame()
        
        # Fallback if image failed to load
        if first_frame is None:
            print("CRITICAL ERROR: No images loaded. Check your assets folder!")
            self.root.destroy()
            return

        self.label = tk.Label(self.root, image=first_frame, bg='#ff00ff', bd=0)
        self.label.pack()

        # Bindings
        self.root.bind("<Button-3>", self.quit_app)
        self.label.bind("<Button-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.do_drag)
        self.label.bind("<ButtonRelease-1>", self.stop_drag)

        # Setup Brain
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        santa_h = first_frame.height()
        floor_y = screen_h - santa_h - config.BOTTOM_OFFSET
        
        self.brain = SantaBehavior(screen_w, floor_y)

        # Start Loops
        self.update_movement()
        self.update_animation()

    def setup_window(self):
        self.root.overrideredirect(True)
        self.root.config(bg='#ff00ff')
        self.root.wm_attributes("-transparentcolor", "#ff00ff")
        self.root.wm_attributes("-topmost", True)

    def start_drag(self, event):
        self.brain.start_drag(event.x_root, event.y_root)

    def do_drag(self, event):
        x, y = self.brain.update_drag(event.x_root, event.y_root)
        self.root.geometry(f"+{x}+{y}")

    def stop_drag(self, event):
        self.brain.end_drag()

    def update_movement(self):
        current_state = self.brain.state
        
        if current_state in ['WALK_LEFT', 'WALK_RIGHT', 'IDLE']:
            new_x, new_y = self.brain.calculate_next_step(config.SPEED)
            self.root.geometry(f"+{new_x}+{new_y}")
            self.root.after(config.MOVEMENT_DELAY, self.update_movement)
            
        elif current_state == 'FALLING':
            new_x, new_y = self.brain.apply_gravity(config.GRAVITY)
            self.root.geometry(f"+{new_x}+{new_y}")
            self.root.after(config.FALL_DELAY, self.update_movement)
            
        elif current_state == 'DRAGGING':
            self.root.after(config.MOVEMENT_DELAY, self.update_movement)

        # UPDATE ANIMATION STATE
        self.animator.set_state(current_state)

    def update_animation(self):
        frame = self.animator.next_frame()
        if frame:
            self.label.config(image=frame)
           
        # --- NEW LOGIC ---
        # Look up the correct delay for the CURRENT state
        # If the state isn't found, default to 100ms
        current_state = self.brain.state
        delay = config.ANIMATION_DELAYS.get(current_state, 100)

        self.root.after(delay, self.update_animation)

    def quit_app(self, event):
        self.root.destroy()
        return "break"