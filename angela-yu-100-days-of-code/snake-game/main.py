from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create 3-unit square length snake
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)


# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

# Using a for loop to create segments
starting_positions = [(0,0), (-20, 0), (-40,0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


screen.exitonclick()
