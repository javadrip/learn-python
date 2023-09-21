import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"), fill="black"
)
card_word = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"), fill="black"
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(
    image=cross_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    command=next_card,
)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(
    image=check_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    command=next_card,
)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
