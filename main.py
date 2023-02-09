import math
import turtle
from random import random

def show_player(t, color, size):
    t.fillcolor(color)
    t.pencolor(color)

    t.begin_fill()
    for i in range (3):
        t.forward(size)
        t.right(120)
    t.end_fill()


def show_circle(t, color, pencolor, radius):
    t.pencolor(pencolor)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def up():
   t1.setheading(90)


def down():
    t1.setheading(270)


def left():
    t1.setheading(180)

def right():
    t1.setheading(0)

def pu():
   t2.setheading(90)


def nwod():
    t2.setheading(270)


def tfel():
    t2.setheading(180)


def thgir():
    t2.setheading(0)

def showLives(num, writecolor):
    turtle.color(writecolor)
    turtle.setposition(-50, 250)
    text = "Lives = " + str(num)
    print(num, "lives left")
    turtle.clear()
    if (lives > 0):
        turtle.write(text, move=False, align="left", font=("Arial", 25, "normal"))
    else:
        turtle.write("Game over", move=False, align="left", font=("Arial", 25, "normal"))
    turtle.hideturtle()


if __name__ == '__main__':
    lives = 3
    t1 = turtle.Turtle()
    t1.speed(10000)

    t1.hideturtle()

    t2 = turtle.Turtle()
    t2.speed(10000)
    t2.hideturtle()

    s = turtle.Screen()
    s.bgcolor("Black")
    s.tracer(0)
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 600
    RADIUS = 25

    s.setup(SCREEN_HEIGHT, SCREEN_WIDTH)
    s.listen()
    s.onkey(up, 'Up')
    s.onkey(down, 'Down')
    s.onkey(left, 'Left')
    s.onkey(right, 'Right')
    s.onkey(pu, 'w')
    s.onkey(nwod, 's')
    s.onkey(tfel, 'a')
    s.onkey(thgir, 'd')
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    step = 0.1
    t1.setheading(90)
    ballcolor = "yellow"
    showLives(3, ballcolor)

    for i in range(1000000000000000000000):
        t1.clear()
        t2.clear()
        show_player(t1, "green", 30)
        show_circle(t2, ballcolor, ballcolor, RADIUS)
        s.update()
        t1.forward(step)


        plr_heading = t1.heading()
        if int(plr_heading) == 0:
            x1 = x1 + step
        elif int(plr_heading) == 180:
            x1 = x1 - step
        elif int(plr_heading) == 90:
            y1 = y1 + step
        elif int(plr_heading) == 270:
            y1 = y1 - step



        if x1 >= SCREEN_WIDTH / 2:
            x1 = -SCREEN_WIDTH / 2
            t1.goto(x1, y1)
            t1.forward(step)
        elif x1 <= -SCREEN_WIDTH / 2:
            x1 = SCREEN_WIDTH / 2
            t1.goto(x1, y1)
            t1.forward(-step)

        if y1 >= SCREEN_HEIGHT / 2:
            y1 = -SCREEN_HEIGHT / 2
            t1.goto(x1, y1)
            t1.forward(step)
        elif y1 <= -SCREEN_HEIGHT / 2:
            y1 = SCREEN_HEIGHT / 2
            t1.goto(x1, y1)
            t1.forward(-step)


        dX = x2 - x1
        dY = y2 - y1
        if dX != 0:
            t2.setheading(math.atan(dY)/dX)

        #print(dX, dY)
        if (i%900 == 0):
            if(abs(dX) < 50):
                if (abs(dY) < 50):
                    if lives == 2:
                        t1.speed(20000)
                        ballcolor = "blue"
                        showLives(2, ballcolor)
                    elif lives == 1:
                        t1.speed(30000)
                        ballcolor = "red"
                        showLives(1, ballcolor)
                    elif lives == 0:
                        print("Game Over")
                        showLives(0, ballcolor)
                        break
                    lives = lives - 1

        ball_heading = t2.heading()
        randx = random()*50
        randy = random() * 100
        if i%2000 == 0:
            x2 = x1 - randx
            y2 = y1 - randy
            t2.goto(x2, y2)

    turtle.mainloop()

