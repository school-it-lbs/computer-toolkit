import turtle

def draw_demo3():
    window = turtle.Screen()
    window.tracer(0)
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.hideturtle()    
    turtle.bgcolor("black")  
    pen.pensize(2)

    initial_size = 30  

    for i in range(200):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(59)

    window.update()


draw_demo3()

turtle.done()
