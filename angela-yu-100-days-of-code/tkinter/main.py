from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
# my_label.config(text="New text")

def button_clicked():
    my_label.config(text="Button got clicked")
    # Line below works too
    # my_label["text"] = "Button got clicked"

button = Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
