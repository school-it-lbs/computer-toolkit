import turtle

def draw_demo2():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(0)
    turtle.bgcolor("black")  
    pen.pensize(2)

    initial_size = 30  

    for i in range(200):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(59)

    pen.hideturtle()


draw_demo2()

turtle.done()
