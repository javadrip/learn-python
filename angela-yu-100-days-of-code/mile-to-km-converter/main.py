from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

input = Entry()
input.grid(row=0, column=1)

miles = Label(text="Miles", font=("Arial", 24))
miles.grid(row=0, column=2)

window.mainloop()
