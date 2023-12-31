from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry()
input.grid(row=0, column=1)

miles = Label(text="Miles", font=("Arial", 24))
miles.grid(row=0, column=2)

equal = Label(text="is equal to", font=("Arial", 24))
equal.grid(row=1, column=0)

converted_value = Label(text="0", font=("Arial", 24))
converted_value.grid(row=1, column=1)

km = Label(text="Km", font=("Arial", 24))
km.grid(row=1, column=2)


def convert():
    new_value = float(input.get()) * 1.609344
    converted_value.config(text=new_value)


calculate = Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)

window.mainloop()
