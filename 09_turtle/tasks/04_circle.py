import turtle

pen = turtle.Turtle()


turtle.bgcolor("black") # set background color of window
pen.pensize(10) # change pen size

pen.color("purple")
pen.circle(100) # draw circle

pen.color("green")
pen.circle(200)

pen.color("red")
pen.circle(-150, extent = 180) # stop drawing at 180 degrees

pen.color("blue")
pen.circle(-100, steps = 5) # draw circle in steps, here a pentagon



turtle.done()
