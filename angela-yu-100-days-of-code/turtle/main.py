# Use Conda interpreter if the screen is buggy

import random
from turtle import Screen, Turtle

t = Turtle()

# Draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# Draw dotted line
# for _ in range(20):
#     t.forward(5)
#     t.penup()
#     t.forward(5)
#     t.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon overlaid over each other
colours = [
    "blue",
    "navy",
    "sea green",
    "lime green",
    "gold",
    "maroon",
    "red",
    "medium violet red",
    "dark violet",
    "indigo",
    "gray",
]

for i in range(3, 11):
    t.color(random.choice(colours))
    for j in range(i):
        t.forward(100)
        angle = 360 / i
        t.right(angle)


screen = Screen()
screen.exitonclick()
