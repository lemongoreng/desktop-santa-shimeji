import os
import sys

# --- PHYSICS SETTINGS ---
SPEED = 3
GRAVITY = 20
MOVEMENT_DELAY = 50
FALL_DELAY = 20         # <--- ADD THIS LINE BACK (Controls falling smoothness)
BOTTOM_OFFSET = 40
SCALE_FACTOR = 4

# --- ANIMATION SPEEDS ---
ANIMATION_DELAYS = {
    'WALK_LEFT':  300,
    'WALK_RIGHT': 300,
    'IDLE':       300,
    'FALLING':    50,
    'DRAGGING':   100,
}

# --- PATH HELPER ---
def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.join(sys._MEIPASS, 'assets')
    else:
        current_dir = os.path.dirname(__file__)
        base_path = os.path.join(current_dir, 'assets')
    return os.path.join(base_path, filename)