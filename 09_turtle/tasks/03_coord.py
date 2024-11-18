import turtle

pen = turtle.Turtle()


def draw_line():
    pen.forward(200)
    pen.stamp() # makes stamp of cursor
    pos = pen.position() # get current position
    pen.write(f" pos: {pos}", font=("Courier", 12, "bold")) # write to screen
    pen.home() # go back to center of screen

def draw_coord():
    draw_line()
    pen.left(90)
    draw_line()
    pen.left(180)
    draw_line()
    pen.left(270)
    draw_line()
    pen.hideturtle() # hide cursor

def draw_dot():
    pen.goto(-100, -100) # go to X/Y coordinates
    pen.color("red") # change color
    pen.dot(10) # draw a dot with n pixel diameter
    pen.write(f" pos: {pen.position()}", font=("Courier", 12, "bold"))

#start drawing
draw_coord()
draw_dot()


turtle.done()