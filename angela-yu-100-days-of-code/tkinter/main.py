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

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Keep window open
window.mainloop()
