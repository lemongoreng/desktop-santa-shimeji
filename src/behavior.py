import random

class SantaBehavior:
    def __init__(self, screen_width, floor_y):
        self.screen_width = screen_width
        self.floor_y = floor_y
        self.x = random.randint(0, screen_width - 100)
        self.y = floor_y
        
        self.target_x = None
        self.pick_new_target()
        
        # Default state
        self.state = 'IDLE'
        self.idle_counter = 0
        
        # Drag offsets
        self.offset_x = 0
        self.offset_y = 0

    def pick_new_target(self):
        self.target_x = random.randint(0, self.screen_width - 100)

    def start_drag(self, mouse_x, mouse_y):
        self.state = 'DRAGGING'
        self.offset_x = mouse_x - self.x
        self.offset_y = mouse_y - self.y

    def update_drag(self, mouse_x, mouse_y):
        self.x = mouse_x - self.offset_x
        self.y = mouse_y - self.offset_y
        return int(self.x), int(self.y)

    def end_drag(self):
        self.state = 'FALLING'

    def apply_gravity(self, gravity_force):
        self.y += gravity_force
        if self.y >= self.floor_y:
            self.y = self.floor_y
            # When he lands, he goes to Idle for a moment
            self.state = 'IDLE'
            self.idle_counter = 10
        return int(self.x), int(self.y)

    def calculate_next_step(self, speed):
        # 1. IDLE LOGIC
        if self.state == 'IDLE':
            self.idle_counter -= 1
            if self.idle_counter <= 0:
                self.pick_new_target() # Pick new spot
                # Decide direction immediately so we don't get stuck in IDLE
                if self.target_x > self.x:
                    self.state = 'WALK_RIGHT'
                else:
                    self.state = 'WALK_LEFT'
            return int(self.x), int(self.y)

        # 2. WALKING LOGIC (LEFT OR RIGHT)
        if self.state in ['WALK_LEFT', 'WALK_RIGHT']:
            dist_x = self.target_x - self.x

            if abs(dist_x) < 5:
                # Arrived! Switch to IDLE
                self.state = 'IDLE'
                self.idle_counter = random.randint(20, 100)
            else:
                # Determine Direction
                if dist_x > 0:
                    self.x += speed
                    self.state = 'WALK_RIGHT'
                else:
                    self.x -= speed
                    self.state = 'WALK_LEFT'
            
            self.y = self.floor_y
            return int(self.x), int(self.y)
            
        return int(self.x), int(self.y)