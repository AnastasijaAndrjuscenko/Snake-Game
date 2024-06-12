from turtle import Turtle

COLOR = "white"
STYLE = ('Courier', 24, 'normal')
ALIGNMENT = 'center'
POSITION_OF_TEXT = (0, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color(COLOR)
        self.penup()
        self.goto(POSITION_OF_TEXT)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=STYLE)

    def count_points(self):
        self.points += 1
        self.clear()
        self.update_scoreboard()
