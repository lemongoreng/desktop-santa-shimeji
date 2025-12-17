import random

class SantaBehavior:
    def __init__(self, screen_width, floor_y):
        self.screen_width = screen_width
        self.floor_y = floor_y
        
        # Coordinates
        self.x = random.randint(0, screen_width - 100)
        self.y = floor_y
        
        # Movement Targets
        self.target_x = None
        self.pick_new_target()
        
        # State: 'WALKING', 'DRAGGING', 'FALLING'
        self.state = 'WALKING'
        
        # For dragging
        self.offset_x = 0
        self.offset_y = 0

    def pick_new_target(self):
        self.target_x = random.randint(0, self.screen_width - 100)

    def start_drag(self, mouse_x, mouse_y):
        self.state = 'DRAGGING'
        # Calculate the distance between the mouse and Santa's top-left corner
        # This ensures he doesn't "teleport" to center on the mouse when clicked
        self.offset_x = mouse_x - self.x
        self.offset_y = mouse_y - self.y

    def update_drag(self, mouse_x, mouse_y):
        # Move Santa to the mouse position, minus the initial grab offset
        self.x = mouse_x - self.offset_x
        self.y = mouse_y - self.offset_y
        return int(self.x), int(self.y)

    def end_drag(self):
        # When released, start falling
        self.state = 'FALLING'

    def apply_gravity(self, gravity_force):
        # Fall down
        self.y += gravity_force
        
        # Check if hit floor
        if self.y >= self.floor_y:
            self.y = self.floor_y
            self.state = 'WALKING' # Resume walking
            
        return int(self.x), int(self.y)

    def calculate_next_step(self, speed):
        # Only walk if we are in the WALKING state
        if self.state != 'WALKING':
            return int(self.x), int(self.y)

        # Normal Walking Logic
        dist_x = self.target_x - self.x

        if abs(dist_x) < 5:
            self.pick_new_target()
        else:
            if dist_x > 0:
                self.x += speed
            else:
                self.x -= speed
        
        # Ensure he stays on the floor (in case of glitches)
        self.y = self.floor_y
        
        return int(self.x), int(self.y)