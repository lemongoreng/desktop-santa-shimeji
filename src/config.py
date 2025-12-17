import os
import sys

# --- SETTINGS ---
SPEED = 1               # Walk speed
SCALE_FACTOR = 4        # Size (Higher = Smaller)
ANIMATION_DELAY = 100
MOVEMENT_DELAY = 50
BOTTOM_OFFSET = 40

# --- PHYSICS SETTINGS ---
GRAVITY = 20            # How fast he falls (pixels per tick)
FALL_DELAY = 20         # How often gravity updates (ms) - lower is smoother

# --- PATH HELPER ---
def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.join(sys._MEIPASS, 'assets')
    else:
        current_dir = os.path.dirname(__file__)
        base_path = os.path.join(current_dir, 'assets')
    return os.path.join(base_path, filename)