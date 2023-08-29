from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
