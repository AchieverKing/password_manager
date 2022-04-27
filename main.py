from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbol + password_letters
    shuffle(password_list)
    gen_pass = "".join(password_list)
    password_button.insert(0, gen_pass)
    pyperclip.copy(gen_pass)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        web1 = web_button.get()
        with open("/Users/PC/OneDrive/Documents/data.json", "r") as pass_json:
            data = json.load(pass_json)
            website1 = data[web1]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No Details For The Website Exist")
    else:
        mail1 = website1["Email"]
        password1 = website1["Password"]
        messagebox.showinfo(title=web1, message=f"Email: {mail1}\nPassword: {password1}")
    finally:
        web_button.delete(0, END)
        password_button.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = web_button.get()
    email = email_user_button.get()
    pas = password_button.get()
    new_text = {
        web: {
            "Email": email,
            "Password": pas
        }
    }

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="opps", message="Please make sure you haven't left any field empty!")
    else:
        """needs to upgrade so i can have authenticator so it can write in google docs"""
        try:
            with open("/Users/PC/OneDrive/Documents/data.json", "r") as pass_list:
                """Reading old file"""
                data = json.load(pass_list)
        except FileNotFoundError:
            with open("/Users/PC/OneDrive/Documents/data.json", "w") as pass_list:
                json.dump(new_text, pass_list, indent=4)
        else:
            """Updating old data with new data"""
            data.update(new_text)
            with open("/Users/PC/OneDrive/Documents/data.json", "w") as pass_list:
                """Saving Updated Data"""
                json.dump(data, pass_list, indent=4)
        finally:
            web_button.delete(0, END)
            password_button.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

"""image_pack"""
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

"""labels"""
website = Label(text="Website:")
website.grid(row=1, column=0)
email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

"""entries"""
web_button = Entry(width=30)
web_button.focus()
web_button.grid(row=1, column=1)
email_user_button = Entry(width=49)
email_user_button.insert(0, "aglhgeneral@gmail.com")
email_user_button.grid(row=2, column=1, columnspan=2)
password_button = Entry(width=30)
password_button.grid(row=3, column=1)

"""buttons"""
gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=3, column=2)
add = Button(text="Add", width=42, command=save)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=15, command=find_password)
search.grid(row=1, column=2)

window.mainloop()
