import turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

window = turtle.Screen()
window.tracer(0)

turtle.bgcolor("black")  

pen = turtle.Turtle()
pen.pensize(2)
pen.hideturtle()
pen.speed(0)

def draw_demo5(rotation):        
    pen.clear()    
    pen.penup()
    pen.home()


    pen.right(rotation)
    pen.backward(100)
    
    for i in range(20):
        pen.color(COLORS[i % 6])

        pen.fillcolor(COLORS[i % 6])
        pen.pendown()
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
        pen.penup()
    
    pen.home()
    pen.color("black")
    pen.dot(220)

rotation = 0


while True:
    draw_demo5(rotation)
    rotation = rotation + 1
    
    window.update()    

turtle.done()
