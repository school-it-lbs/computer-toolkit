import turtle
import time

window = turtle.Screen()
window.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
start = 100


def draw_spiral(n):
    pen.clear()
    pen.penup()
    pen.home()
    pen.down()
    for i in range(100):
        pen.forward(n * i)
        pen.left(90)
        pen.forward(n * i)
        pen.left(90)

while True:
    draw_spiral(start)
    start = start - 1
    if start == 0:
        start = 100
    window.update()
    time.sleep(0.05)

turtle.done()
