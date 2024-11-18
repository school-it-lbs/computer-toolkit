import turtle

pen = turtle.Turtle()

turtle.bgcolor("black")
pen.hideturtle()

pen.speed(0)

DEG = 144
SIZE = 200


def draw_star(x, y, rot, color):
    pen.penup()
    pen.goto(x, y)
    pen.left(rot)
    pen.pendown()
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.forward(SIZE)
    pen.right(DEG)
    pen.forward(SIZE)
    pen.right(DEG)
    pen.forward(SIZE)
    pen.right(DEG)
    pen.forward(SIZE)
    pen.right(DEG)
    pen.forward(SIZE)
    pen.end_fill()



draw_star(100, 100, 32, "red")
draw_star(200, 200, 27, "green")
draw_star(-150, 150, 12, "blue")
draw_star(-400, -400, 12, "cyan")



turtle.done()