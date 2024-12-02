import turtle
import time

class Text:
    FONT = "Courier"
    FONT_WEIGHT = "bold"

    def __init__(self, dimensions):
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.setposition(dimensions.left * 0.8, dimensions.top * 0.8)
        text.color(1, 1, 1)
        self.text = text
        self.game_timer = time.time()

    def write_score(self, score):
        time_elapsed = time.time() - self.game_timer
        self.text.clear()
        self.text.write(
            f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
            font=(self.FONT, 20, self.FONT_WEIGHT),
        )

    def write_game_over(self):
        self.text.home()
        self.text.write("GAME OVER", font=(self.FONT, 40, self.FONT_WEIGHT), align="center")
