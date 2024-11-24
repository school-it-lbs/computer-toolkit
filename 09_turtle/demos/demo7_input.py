import turtle


pen = turtle.Turtle()
pen.hideturtle()

name = turtle.textinput("Name", "Please enter your name:")

pen.write(name, font=("Tahoma", 20, "bold"))

turtle.done()
