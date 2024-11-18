import turtle

def draw_demo1():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(0)
    turtle.bgcolor("black") 
    pen.pensize(2)

    for i in range(35):
        pen.color(colors[i % 6])
        pen.circle(100)
        pen.left(25)

    pen.hideturtle()

draw_demo1()

turtle.done()