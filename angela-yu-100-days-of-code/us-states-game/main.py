import turtle

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

answer_state = screen.textinput(
    title="Guess the state", prompt="What's another state's name?"
)
