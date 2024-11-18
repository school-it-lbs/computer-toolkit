import turtle

window = turtle.Screen()
window.tracer(0)

def draw_demo4():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()    
    pen.speed(0)
    turtle.bgcolor("black")  
    pen.pensize(2)
    pen.hideturtle()

    pen.backward(150)

    for i in range(180):
        pen.color(colors[i % 6])

        pen.fillcolor(colors[i % 6])
        pen.begin_fill()
        pen.forward(200)
        pen.right(61)
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(61)
        pen.forward(200)
        pen.right(181)
        pen.end_fill()
        
    
    pen.home()
    pen.backward(50)
    pen.color("black")
    pen.dot(220)

draw_demo4()

turtle.done()
