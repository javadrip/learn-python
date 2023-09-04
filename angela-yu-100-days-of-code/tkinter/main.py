from tkinter import *

# Initialise window
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Display label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
# my_label.config(text="New text")

# Button click behaviour
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    # Line below works too
    # my_label["text"] = "Button got clicked"

# Display button
button = Button(text="Click me", command=button_clicked)
button.pack()

# Display input field
input = Entry()
input.insert(END, string="Some text to begin with.")
input.pack()

# Keep window open
window.mainloop()
