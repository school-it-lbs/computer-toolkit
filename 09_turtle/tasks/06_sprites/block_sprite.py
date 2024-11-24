import turtle

class BlockSprite:

    # constructor with parameters
    def __init__(self, w, h):
        # self is the instance of the class
        self.w = w
        self.h = h
    
    def draw(self):
        # creates instance of turtle
        pen = turtle.Turtle()
        pen.forward(self.w)
        pen.left(90)
        pen.forward(self.h)
        pen.left(90)
        pen.forward(self.w)
        pen.left(90)
        pen.forward(self.h)
        pen.left(90)
