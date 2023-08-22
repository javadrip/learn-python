import turtle as t

# tim = t.Turtle()
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -140

for color in colors:
    gap = 40
    y += gap
    tim = t.Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y=y)


screen.exitonclick()
