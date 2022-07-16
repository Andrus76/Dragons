import time
from turtle import *

pen = Turtle()
pen.color('red')
bgcolor('black')

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def draw_txt():
    pen.up()
    pen.setpos(-50, 90)
    pen.down()
    pen.color('white')
    pen.write("Люблю тебя", font=("Montserrat", 16, "bold"))
    pen.up()
    pen.setpos(-70, 70)
    pen.down()
    time.sleep(1)

draw_heart()
draw_txt()
done()
import turtle
import math

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 \
           * math.cos(2 * t) - 2 * \
           math.cos(3 * t) - math.cos(4 * t)

t = turtle.Turtle()
t.speed(500)#500
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.goto(0, 0)
t.hideturtle()
turtle.update()
turtle.mainloop()