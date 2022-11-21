import turtle

class Dino:
    def __init__(self, x, y, setting):
        self.x = x
        self.y = y
        self.velocity = 0
        # setting data
        self.gravity = setting.gravity
        self.delta_time = setting.delta_time
        # dino's measurements (acc to image)
        self.height = 50
        self.width  = 50
        # current dino rendering state (for animation)
        self.state_1   = True
        self.cnt_frame = 0

        self.dino  = "dino.gif"
        self.dino1 = "dino2.gif"
        self.dino2 = "dino3.gif"

        self.ground_m_body = setting.ground+self.height/2
        self.stamp = turtle.Turtle()
        self.stamp.shape('dino.gif')
        self.stamp.shapesize(stretch_wid=self.height/20, stretch_len=self.width/20)
        self.stamp.penup()

    def render(self):
        if self.state_1:
            self.stamp.shape(self.dino1)
        else:
            self.stamp.shape(self.dino2)
        if self.cnt_frame > 1/self.delta_time/20:  # change frame 20 times a second
            self.state_1 = not self.state_1
            self.cnt_frame = 0
        self.cnt_frame += 1
        if self.y > self.ground_m_body: self.stamp.shape(self.dino)

        self.update_pos()
        self.stamp.goto(self.x, self.y)

    def update_pos(self):
        self.velocity -= self.gravity*self.delta_time   # add gravity v=u+at
        self.y        += self.velocity*self.delta_time + 1/2*self.gravity*self.delta_time*self.delta_time # s = ut + 1/2gt^2

        if self.y < self.ground_m_body:
            self.y = self.ground_m_body
            self.velocity = 0

    def jump(self):
        if self.y == self.ground_m_body:
            self.velocity += 1000
