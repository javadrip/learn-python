import json
import random
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    # List comprehension to generate random list of letters, symbols and numbers repectively
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Alternative to the three lines commented out below
    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    # checks if fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Make sure there are no empty fields!"
        )
    else:
        # Confirmation popup
        # is_ok = messagebox.askokcancel(
        #     title=website,
        #     message=f"These are the details entered: \nUsername: {username} \nPassword: {password} \nIs it okay to save?",
        # )

        # if is_ok:
        # Using with will close the file automatically without having to end with .close()
        # with open("data.txt", "a") as data_file:
        #     data_file.write(f"{website} | {username} | {password}\n")
        #     website_entry.delete(0, END)
        #     password_entry.delete(0, END)
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No data file found. Have you saved any password yet?",
        )
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Username: {username}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists."
            )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width="200", height="200")
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=23)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)

# Username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(width=41)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "dummyemail@gmail.com")

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# Add
add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
