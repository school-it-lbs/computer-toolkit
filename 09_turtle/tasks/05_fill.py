import turtle

pen = turtle.Turtle()



pen.pensize(5)
pen.hideturtle()
pen.pencolor("purple")
pen.fillcolor("orange")

#draw triangle
pen.begin_fill()
pen.fd(100)
pen.lt(120)
pen.fd(100)
pen.lt(120)
pen.fd(100)
pen.end_fill()

#draw open box
pen.penup()
pen.fillcolor("lime")
pen.goto(200, 200)
pen.pendown()
pen.begin_fill()
pen.goto(200,300)
pen.goto(300,300)
pen.goto(300,200)
pen.end_fill()


turtle.done()