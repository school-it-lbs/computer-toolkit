import turtle

pen = turtle.Turtle()



turtle.bgcolor("black")
pen.hideturtle()
pen.color("yellow")
pen.fillcolor("yellow")

DEG = 144
SIZE = 200

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

pen.home()
pen.penup()
pen.goto(100, -73)
pen.pendown()
pen.begin_fill()
pen.circle(40, steps=5)
pen.end_fill()


turtle.done()