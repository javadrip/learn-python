# Use Conda interpreter if the screen is buggy

from turtle import Screen, Turtle

timmy = Turtle()

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
