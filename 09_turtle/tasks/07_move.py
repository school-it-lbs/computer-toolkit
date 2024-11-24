import turtle

window = turtle.Screen()
window.tracer(0)

window.run = True

# class definition
# start --------------------------------------------------
class Point():
    STEP = 10

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        
        point = turtle.Turtle()
        point.penup()
        point.color("red")
        point.fillcolor("red")
        point.hideturtle()                
        self.point = point
        
    def updatePosition(self):
        self.point.clear()
        self.point.setposition(self.pos_x, self.pos_y)
        
        # draw object
        self.point.pendown()
        self.point.begin_fill()                
        self.point.circle(100)                
        self.point.end_fill()
        self.point.penup()
               
    def move_left(self):
        self.pos_x = self.pos_x - self.STEP    

    def move_right(self):
        self.pos_x = self.pos_x + self.STEP

    def move_up(self):
        self.pos_y = self.pos_y + self.STEP

    def move_down(self):
        self.pos_y = self.pos_y - self.STEP

# end ----------------------------------------------------

def stop():
    window.run = False

point = Point()

window.onkeypress(point.move_left, "Left")
window.onkeypress(point.move_right, "Right")
window.onkeypress(point.move_up, "Up")
window.onkeypress(point.move_down, "Down")
window.onkeypress(stop, "space")

# register event listener
window.listen()


# game loop
while window.run:    
    point.updatePosition()
    window.update()
    if not window.run:
        break

print("done")    
turtle.done()
