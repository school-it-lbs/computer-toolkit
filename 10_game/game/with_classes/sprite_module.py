import turtle
import random

class Laser:
    LASER_LENGTH = 20
    LASER_SPEED = 20

    def __init__(self, cannon):
        self.sprite = turtle.Turtle()
        self.pos_x = cannon.pos_x()
        self.pos_y = cannon.pos_y()
        self.draw()
       
    def draw(self):
        self.sprite.penup()
        self.sprite.color(1, 0, 0)
        self.sprite.hideturtle()
        self.sprite.setposition(self.pos_x, self.pos_y)
        self.sprite.setheading(90)
        # Move laser to just above cannon tip
        self.sprite.forward(20)
        # Prepare to draw the laser
        self.sprite.pendown()
        self.sprite.pensize(5)


    def move(self):
        self.sprite.clear()
        self.sprite.forward(self.LASER_SPEED)
        # Draw the laser
        self.sprite.forward(self.LASER_LENGTH)
        self.sprite.forward(-self.LASER_LENGTH)


class Alien:
    ALIEN_SPEED = 3.5

    def __init__(self, dimensions):
        self.sprite = turtle.Turtle()
        self.dimensions = dimensions
        self.draw()

    def draw(self):
        self.sprite.penup()
        self.sprite.turtlesize(1.5)
        self.sprite.setposition(
            random.randint(
                int(self.dimensions.left + self.dimensions.gutter),
                int(self.dimensions.right - self.dimensions.gutter),
            ),
            self.dimensions.top,
        )
        self.sprite.shape("turtle")
        
        self.sprite.setheading(-90)
        self.sprite.color(random.random(), random.random(), random.random())

    def move(self):
        self.sprite.forward(self.ALIEN_SPEED)


class Cannon:
    CANNON_STEP = 10

    def __init__(self, dimensions):
        self.dimensions = dimensions
        
        sprite = turtle.Turtle()
        sprite.penup()
        sprite.color(1, 1, 1)
        sprite.shape("square")
        sprite.setposition(0, dimensions.floor)
        self.sprite = sprite

        self.movement = 0  # -1, 0 or 1 for left, stationary, right
        
    def draw(self):        
        self.sprite.clear()
        self.sprite.turtlesize(1, 4)  # Base
        self.sprite.stamp()
        self.sprite.sety(self.dimensions.floor + 10)
        self.sprite.turtlesize(1, 1.5)  # Next tier
        self.sprite.stamp()
        self.sprite.sety(self.dimensions.floor + 20)
        self.sprite.turtlesize(0.8, 0.3)  # Tip of cannon
        self.sprite.stamp()
        self.sprite.sety(self.dimensions.floor)

    def move(self):
        new_x = self.sprite.xcor() + self.CANNON_STEP * self.movement
        if self.dimensions.left + self.dimensions.gutter <= new_x <= self.dimensions.right - self.dimensions.gutter:
            self.sprite.setx(new_x)
            self.draw()
    
    def move_left(self):
        self.movement = -1

    def move_right(self):
        self.movement = 1

    def stop_movement(self):
        self.movement = 0

    def pos_x(self):
        return self.sprite.xcor()
    
    def pos_y(self):
        return self.sprite.ycor()