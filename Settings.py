class Settings:
    def __init__(self, width, height, ground, delta_time=1/60, gravity=5000): # 60 FPS default
        self.width = width
        self.height = height
        self.ground = ground
        self.delta_time = delta_time
        self.gravity = gravity
        self.score = 0