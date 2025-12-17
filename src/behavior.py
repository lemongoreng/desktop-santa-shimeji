import random

class SantaBehavior:
    def __init__(self, screen_width, start_y):
        self.screen_width = screen_width
        self.x = random.randint(0, screen_width - 100)
        self.y = start_y
        self.target_x = None
        self.pick_new_target()

    def pick_new_target(self):
        # Pick a random spot, ensuring we don't walk off-screen
        # We subtract 100 as a safe margin for Santa's width
        self.target_x = random.randint(0, self.screen_width - 100)

    def calculate_next_step(self, speed):
        # Logic: Move X towards Target X
        dist_x = self.target_x - self.x

        # If close enough, pick new target
        if abs(dist_x) < 5:
            self.pick_new_target()
        else:
            if dist_x > 0:
                self.x += speed
            else:
                self.x -= speed
        
        return int(self.x), int(self.y)