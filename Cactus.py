import turtle
import random

class Cactus:
    def __init__(self, setting):
        self.positions   =  []
        # Cactus measurements
        self.height      =  40
        self.width       =  18
        # crow measurements
        self.crow_heigth   =  37
        self.crow_width    =  42
        self.crow_height_g =  70

        # crow flapping state (animation)
        self.crow_state = True
        self.cnt_frame  = 0

        self.start_p     =  300
        self.speed       =  6

        # setting data
        self.ground        =    setting.ground
        self.screen_width  =    setting.width
        self.delta_time    =    setting.delta_time
        self.ground_m_body =    setting.ground+self.height/2

        # instantiating initial cactus chunk
        for i in range(10):
            self.positions.append(self.make_chunk())

        # turtle for cactus itself
        self.stamper = turtle.Turtle()
        self.stamper.penup()
    
    def make_chunk(self): # return type: (no of obj, distance after, type of obj(1=Cactus, 2=crow))
        if random.random() < 0.2: # assuming 20% chance of getting crow
            return (1, random.randint(150, 300), 2)
        # else normal cactus
        return (random.randint(1,3), random.randint(150, 300), 1)

    def render(self, dino):
        self.stamper.clear() # clearing previous instance of objects

        # crow animation setter
        if self.cnt_frame > 1/self.delta_time/10: # crow flaps 10 times a second
            self.crow_state = not self.crow_state
            self.cnt_frame = 0
        self.cnt_frame += 1

        # if start position is < screen_width, remove first obj and append new chunk
        if self.start_p < -400:
            self.start_p   +=  self.positions[0][0]*self.width + self.positions[0][1]
            self.positions  =  self.positions[1:]
            self.positions.append(self.make_chunk())
            
        # a pointer to start rendering new obj
        pointer = self.start_p
        collision = False
        for i in range(len(self.positions)):
            # checking for collision
            if self.rect_rect_coll(dino.x, dino.y, dino.width, dino.height, self.positions[i][0], pointer, self.positions[i][-1]):
                collision = True

            # main rendering
            for j in range(self.positions[i][0]):
                if self.positions[i][-1] == 1:
                    self.stamper.goto(pointer, self.ground_m_body)
                    self.stamper.shape('images/cactus.gif')
                else:
                    self.stamper.goto(pointer, self.ground + self.crow_height_g)
                    if self.crow_state:
                        self.stamper.shape('images/crow.gif')
                    else:
                        self.stamper.shape('images/crow2.gif')

                self.stamper.stamp()
                pointer += self.width
            pointer += self.positions[i][1]

            if pointer > self.screen_width:      # just optimizing a bit
                break

        self.start_p -=  self.speed
        self.speed   +=  0.1*self.delta_time

        return collision

    # collision detection (false assumptions)
    def rect_rect_coll(self, x1, y1, w, h, n, p, type_o):
        # for Cactus
        if type_o == 1:
            if x1+w/3 < p-self.width/2: return False        # DD   CCC
            if x1-w/3 > p+(n-0.5)*self.width: return False  # CCC   DD
            if y1-h/2 > self.ground+self.height: return False
            return True
        
        # for Crow
        if x1+w/2 < p-self.crow_width/2: return False       # DD CC
        if x1-w/2 > p+self.crow_width/2: return False       # CC DD
        if y1+h/2 < self.ground+self.crow_height_g-self.crow_heigth/2: return False
        return True
