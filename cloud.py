import turtle
import random

class Cloud:
    def __init__(self, setting):
        self.width = setting.width
        self.height = setting.height
        self.start_pos = random.randint(-self.width, 0)
        self.cloud = []
        for i in range(10):
            self.cloud.append(self.generate_cloud())
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.shape('images/cloud.gif')
    
    def generate_cloud(self): # returns (y-level, distance)
        return [random.randint(0, self.height//4), random.randint(120, self.width/2)]

    def render(self):
        self.pen.clear()
        pointer = self.start_pos

        if pointer < -self.width:
            pointer += self.cloud[0][-1]
            self.start_pos = pointer
            self.cloud = self.cloud[1:]
            self.cloud.append(self.generate_cloud())

        for y, distance in self.cloud:
            self.pen.goto(pointer, y)
            self.pen.stamp()
            pointer+=distance
        
        self.start_pos -= 1