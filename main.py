import turtle
import time

from Settings import Settings
from Dino import Dino
from Cactus import Cactus
from cloud import Cloud

highscore = int(open("highscore.txt",'r').read())

setting = Settings(width=600, height=400, ground=-130) # instantiating settings

# setting up screen
Screen = turtle.Screen()
Screen.tracer(0,0)
Screen.setup(setting.width, setting.height)

# registering images (dino and cactus)
Screen.register_shape('images/dino.gif')
Screen.register_shape('images/dino2.gif')
Screen.register_shape('images/dino3.gif')
Screen.register_shape('images/cactus.gif')
Screen.register_shape('images/crow.gif')
Screen.register_shape('images/crow2.gif')
Screen.register_shape('images/cloud.gif')



def play():
    global highscore

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
    cloud  = Cloud(setting)

    draw_board()

    while True:
        # score stuff
        setting.score += setting.delta_time
        score_writer.clear()

        highscore = max(highscore, int(setting.score*10))
        score_writer.write(f"HI {highscore:04}, {int(setting.score*10):04}") # per second score kinda felt slow LOL

        # event listeners
        Screen.onkey(dino.jump, 'Up')
        Screen.onkey(dino.jump, 'space')

        # rendering
        cloud.render()
        dino.render()
        if cactus.render(dino): # cactus.render returns false when dino collides with cactus
            break

        # frame rate delays
        time.sleep(setting.delta_time)
        Screen.update()
    open("highscore.txt", "w").write(str(highscore))

if __name__ == "__main__":
    while True:
        play()
        time.sleep(2)
        Screen.clear()
        Screen.tracer(0,0)
    Screen.mainloop()
