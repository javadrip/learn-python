# Use Conda interpreter if the screen is buggy

import random
import turtle as t

tim = t.Turtle()

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# Draw dotted line
# for _ in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon overlaid over each other
# colours = [
#     "blue",
#     "navy",
#     "sea green",
#     "lime green",
#     "gold",
#     "maroon",
#     "red",
#     "medium violet red",
#     "dark violet",
#     "indigo",
#     "gray",
# ]

# for i in range(3, 11):
#     tim.color(random.choice(colours))
#     for j in range(i):
#         tim.forward(100)
#         angle = 360 / i
#         tim.right(angle)


# Draw a random walk
# colours = [
#     "blue",
#     "navy",
#     "sea green",
#     "lime green",
#     "gold",
#     "maroon",
#     "red",
#     "medium violet red",
#     "dark violet",
#     "indigo",
#     "gray",
# ]

# tim.hideturtle()
# tim.width(10)
# tim.speed(0)
# angle = [0, 90, 180, 270]

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(20)
#     tim.setheading(random.choice(angle))

# Draw a random walk with random rgb colours
# t.colormode(255)


# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colour = (r, g, b)
#     return colour


# tim.hideturtle()
# tim.width(10)
# tim.speed(0)
# angle = [0, 90, 180, 270]

# for _ in range(200):
#     tim.color(random_colour())
#     tim.forward(20)
#     tim.setheading(random.choice(angle))

# Draw a spirograph
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


tim.speed(0)


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw_spirograph(10)


screen = t.Screen()
screen.exitonclick()
