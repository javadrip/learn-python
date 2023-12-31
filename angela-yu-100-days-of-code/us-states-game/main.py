import turtle

import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


# Console log the coordinates of the mouse click
# def get_mouse_click_coord(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
# Need to covert to list to use if loop.
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 states correct",
        prompt="What's another state's name? (Type 'Exit' to exit the game)",
    ).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


print(missing_states)
