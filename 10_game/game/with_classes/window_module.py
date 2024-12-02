import time
import turtle
import game_module

class Dimensions:
    def __init__(self, window_width, window_height):
        self.left = -window_width / 2
        self.right = window_width / 2
        self.top = window_height / 2
        self.bottom = -window_height / 2
        self.floor = 0.9 * self.bottom
        self.gutter = 0.025 * window_width

class Window:
    FRAME_RATE = 30  # Frames per second
    TIME_FOR_1_FRAME = 1 / FRAME_RATE  # Seconds


    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.tracer(0)
        self.screen.setup(0.5, 0.75)
        self.screen.bgcolor(0.2, 0.2, 0.2)
        self.screen.title("The Real Python Space Invaders")

        self.dimensions = Dimensions(self.screen.window_width(), self.screen.window_height())                
        self.game = game_module.Game(self.dimensions, self.screen)
                        

    def frame_limiter(self, func):
            timer_this_frame = time.time()

            func()
            
            time_for_this_frame = time.time() - timer_this_frame
            if time_for_this_frame < self.TIME_FOR_1_FRAME:
                time.sleep(self.TIME_FOR_1_FRAME - time_for_this_frame)
            self.screen.update()


    def run(self):
        while self.game.game_running:
            self.frame_limiter(self.game.render)
        self.game.game_over()
        turtle.done()