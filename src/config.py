import os

# --- SETTINGS ---
SPEED = 1               # Speed of movement
SCALE_FACTOR = 4        # 1/4th size
ANIMATION_DELAY = 100   # ms between frames
MOVEMENT_DELAY = 50     # ms between movement updates
BOTTOM_OFFSET = 10      # Distance from the very bottom of the screen

# --- PATH HELPER ---
def get_asset_path(filename):
    # This ensures we always find the asset relative to this file
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'assets', filename)