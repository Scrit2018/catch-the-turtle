import time
import turtle
import math
import random

## Creat the score variable
clicks = 0

#Create the time variable
time_limit = 20

# Set up screen
wn = turtle.Screen()
wn.bgcolor("light green")

# Score Pen Create
scorePen = turtle.Turtle()
scorePen.hideturtle()
scorePen.penup()
scorePen.goto(-200,300)
scorePen.write(f"Score: {clicks}", align="center", font=('monaco', 20, 'bold'))

# Time Pen Create
timePen = turtle.Turtle()
timePen.hideturtle()
timePen.penup()
timePen.goto(-200,250)
timePen.write(f"Time: {time_limit}", align="center", font=('monaco', 20, 'bold'))

# Game Over Pen Create
gameovenPen = turtle.Turtle()
gameovenPen.hideturtle()
gameovenPen.penup()

# TurtleObject Create
turtleObject = turtle.Turtle()
image = "turtle.gif"
turtle.addshape(image)
turtleObject.shape(image)
turtleObject.penup()

# Functions Create
def add_mouse_listener():
    def on_motion(event):
        nonlocal x, y
        x = event.x - wn.window_width() / 2
        y = -event.y + wn.window_height() / 2

    turtle.getcanvas().bind('<Motion>', on_motion)
    x, y = -100, 200
    return lambda: (x, y)

def click_eneble(x, y):
    global clicks
    clicks += 1
    scorePen.clear()
    scorePen.write(f"Score: {clicks}", align="center", font=('monaco', 20, 'bold'))

def click_disable(x, y):
    pass

start_time = time.time()

while True:
    mouse_pos = add_mouse_listener()
    frame_delay_ms = 1000 // random.randint(2,30)
    wn.tracer(3)
    def play():
        global clicks
        elapsed_time = time.time() - start_time
        timer = time_limit - int(elapsed_time)
        if not int(elapsed_time) > time_limit:
            timePen.clear()
            timePen.write(f"Time: {timer}", align="center", font=('monaco', 20, 'bold'))
            turtleObject.onclick(click_eneble)

            x, y = mouse_pos()
            detent = math.sqrt(math.pow(turtleObject.xcor() - x,2) + math.pow(turtleObject.ycor() - y,2))
            if detent < 50:
                turtleObject.hideturtle()
                turtleObject.goto(random.randint(-200,200), random.randint(-200,200))
            else:
                turtleObject.showturtle()
            wn.ontimer(play, frame_delay_ms)
            wn.update()
        else:
            gameovenPen.write("GAME OVER", align="center", font=('monaco', 20, 'bold'))
            turtleObject.onclick(click_disable)
            #wn.exitonclick()

    play()
    wn.mainloop()