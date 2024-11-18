import turtle

pen = turtle.Turtle()

pen.speed(0)
pen.hideturtle()

pen.pensize(10)
pen.color("purple")
pen.penup()
pen.goto(0, -400)
pen.pendown()
pen.circle(400)

pen.penup()
pen.home()

pen.pensize(8)
pen.color("red")
pen.goto(0, -300)
pen.pendown()
pen.circle(300)

pen.penup()
pen.home()

pen.pensize(6)
pen.color("orange")
pen.goto(0, -200)
pen.pendown()
pen.circle(200)

pen.penup()
pen.home()

pen.pensize(4)
pen.color("pink")
pen.goto(0, -100)
pen.pendown()
pen.circle(100)

pen.penup()
pen.home()

pen.pensize(2)
pen.color("blue")
pen.goto(0, -50)
pen.pendown()
pen.circle(50)

turtle.done()
