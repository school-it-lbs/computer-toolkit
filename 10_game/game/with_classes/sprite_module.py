import turtle
import random
import time

class Enemy:
    def __init__(self, dimensions, speed):
        self.sprite = turtle.Turtle()
        self.dimensions = dimensions
        self.speed = speed

    def set_random_color(self):
        self.sprite.color(random.random(), random.random(), random.random())

    def set_random_position(self):
        self.sprite.setposition(
                random.randint(
                    int(self.dimensions.left + self.dimensions.gutter),
                    int(self.dimensions.right - self.dimensions.gutter),
                ),
                self.dimensions.top,
            )


class Alien(Enemy):
    def __init__(self, dimensions):
        Enemy.__init__(self, dimensions, 3.5)
        self.draw()

    def draw(self):
        self.sprite.penup()
        self.sprite.turtlesize(1.5)
        self.set_random_position()
        self.sprite.shape("circle")
        
        self.sprite.setheading(-90)
        self.set_random_color()

    def move(self):
        self.sprite.forward(self.speed)
     
     
class Ufo(Enemy):
    KEEP_DIRECTION_IN_SEC = 1

    def __init__(self, dimensions):
        Enemy.__init__(self, dimensions, 5)
        self.heading = [-45, -90, -135]
        self.timer = time.time()
        self.last_heading = self.heading[1]
        self.sprite.pensize(2)
        self.set_random_color()
        self.sprite.hideturtle()
        self.set_random_position()

    def draw(self):
        self.sprite.clear()
        self.sprite.forward(-8)
        self.sprite.dot(10)
        self.sprite.forward(8)
        self.sprite.setheading(0)
        self.sprite.pendown()
        self.sprite.circle(20)
        self.sprite.penup()
        self.sprite.forward(10)
        self.sprite.left(90)
        self.sprite.forward(20)
        self.sprite.pendown()
        self.sprite.circle(10)
        self.sprite.penup()
        self.sprite.forward(-20)
        self.sprite.left(-90)
        self.sprite.forward(-10)
        self.sprite.setheading(self.last_heading) 
        
    def move(self):
        self.sprite.forward(self.speed)
        self.draw()
        now = time.time()        
        if(now - self.timer > self.KEEP_DIRECTION_IN_SEC):
            self.timer = now
            self.last_heading = self.heading[random.randint(0, 2)]
        self.sprite.setheading(self.last_heading)        


class Rocket(Enemy):
    KEEP_DIRECTION_IN_SEC = 0.5

    def __init__(self, dimensions):
        Enemy.__init__(self, dimensions, 4)
        self.heading = [-45, -67.5, -90, -112.5, -135]
        self.timer = time.time()
        self.last_heading = self.heading[2]        
        self.draw()

    def draw(self):
        self.sprite.penup()
        self.sprite.pensize(2)
        self.set_random_color()        
        self.set_random_position()
        self.sprite.pendown()
        self.sprite.shape("classic")
        
    def move(self):
        self.sprite.forward(self.speed)
        now = time.time()        
        if(now - self.timer > self.KEEP_DIRECTION_IN_SEC):
            self.timer = now
            self.last_heading = self.heading[random.randint(0, 4)]
        self.sprite.setheading(self.last_heading)     


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