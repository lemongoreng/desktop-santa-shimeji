import os
import sys

# --- SETTINGS ---
SPEED = 1               # Speed of movement
SCALE_FACTOR = 4        # 1/4th size
ANIMATION_DELAY = 100   # ms between frames
MOVEMENT_DELAY = 50     # ms between movement updates
BOTTOM_OFFSET = 10      # Distance from the very bottom of the screen

# --- PATH HELPER ---
def get_asset_path(filename):
    # Check if we are running as a compiled .exe
    if hasattr(sys, '_MEIPASS'):
        # If yes, PyInstaller extracts assets to this temp folder
        base_path = os.path.join(sys._MEIPASS, 'assets')
    else:
        # If no, we are just running normal Python code
        current_dir = os.path.dirname(__file__)
        base_path = os.path.join(current_dir, 'assets')
    
    return os.path.join(base_path, filename)