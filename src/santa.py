import tkinter as tk
import os

class DesktopSanta:
    def __init__(self, root):
        self.root = root

        # --- UPDATED PATH SETUP ---
        # Get the path to this file (src/santa.py)
        current_dir = os.path.dirname(__file__)
        
        # 'assets' is now directly inside the current directory
        # No more ".." needed!
        image_path = os.path.join(current_dir, 'assets', 'santa.gif')
        
        # --- LOAD IMAGE ---
        try:
            self.img = tk.PhotoImage(file=image_path)
        except Exception as e:
            print(f"Error: Could not find image at {image_path}")
            return

        # --- WINDOW CONFIG ---
        self.root.overrideredirect(True)
        self.root.config(bg='black')
        self.root.wm_attributes("-transparentcolor", "black")
        self.root.wm_attributes("-topmost", True)
        
        self.label = tk.Label(self.root, image=self.img, bg='black', bd=0)
        self.label.pack()
        
        # NEW: Bind right-click to close the app
        # <Button-3> is the code for Right-Click on Windows
        self.root.bind("<Button-3>", self.quit_app)

        # Screen Dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Initial State
        self.x = 0
        self.y = 0
        self.speed = 4
        self.direction = 'top' 
        
        self.update_position()

    def update_position(self):
        w = self.img.width()
        h = self.img.height()

        # Movement Logic
        if self.direction == 'top':
            self.x += self.speed
            self.y = 0
            if self.x >= self.screen_width - w:
                self.direction = 'right'
                
        elif self.direction == 'right':
            self.x = self.screen_width - w
            self.y += self.speed
            if self.y >= self.screen_height - h:
                self.direction = 'bottom'
                
        elif self.direction == 'bottom':
            self.x -= self.speed
            self.y = self.screen_height - h
            if self.x <= 0:
                self.direction = 'left'
                
        elif self.direction == 'left':
            self.x = 0
            self.y -= self.speed
            if self.y <= 0:
                self.direction = 'top'

        self.root.geometry(f'{w}x{h}+{self.x}+{self.y}')
        self.root.after(50, self.update_position)
        
        def quit_app(self, event):
            self.root.quit()