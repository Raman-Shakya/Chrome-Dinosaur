import turtle
import time

from Settings import Settings
from Dino import Dino
from Cactus import Cactus

setting = Settings(width=600, height=400, ground=-130) # instantiating settings

# setting up screen
Screen = turtle.Screen()
Screen.tracer(0,0)
Screen.setup(setting.width, setting.height)

# registering images (dino and cactus)
Screen.register_shape('dino.gif')
Screen.register_shape('dino2.gif')
Screen.register_shape('dino3.gif')
Screen.register_shape('cactus.gif')
Screen.register_shape('crow.gif')
Screen.register_shape('crow2.gif')



pen = turtle.Turtle()

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.goto(0, setting.height/4)


def draw_board(): # just draws a straight line representing ground
    pen.penup()
    pen.goto(-setting.width, setting.ground)
    pen.pendown()
    pen.goto(setting.width, setting.ground)


Screen.listen()
setting.score = 0

# instantiating dino and cactus
dino = Dino(0, 0, setting)
cactus = Cactus(setting)

draw_board()

while True:
    # score stuff
    setting.score += setting.delta_time
    score_writer.clear()
    score_writer.write(int(setting.score*10)) # per second score kinda felt slow LOL

    # event listeners
    Screen.onkey(dino.jump, 'Up')
    Screen.onkey(dino.jump, ' ')

    # rendering
    dino.render()
    if cactus.render(dino): # cactus.render returns false when dino collides with cactus
        break

    # frame rate delays
    time.sleep(setting.delta_time)
    Screen.update()

Screen.mainloop()