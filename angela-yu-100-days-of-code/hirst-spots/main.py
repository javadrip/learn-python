# import colorgram

# number_of_colors = 10

# colors = colorgram.extract("image.png", number_of_colors)

# rgb_colors = []

# for color in colors:
#     combination = ()
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)

#     rgb_colors.append(new_color)

# print(rgb_colors)

import random
import turtle as t

t.colormode(255)

color_list = [
    (204, 165, 107),
    (239, 246, 241),
    (151, 73, 47),
    (235, 238, 243),
    (223, 202, 135),
    (172, 154, 38),
    (51, 93, 125),
    (137, 31, 21),
]

tim = t.Turtle()

tim.penup()
tim.speed(0)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
