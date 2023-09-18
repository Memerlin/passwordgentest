import tkinter.simpledialog
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from passwordgen import generate_password

# This is built with tkinter version 8.6.12
root = Tk()
root.title("Jim's password generator!")

passwords = []  # Here the generated passwords will save


def thank_you():
    answer = tkinter.messagebox.askyesno(title="Done!",
                                         message="The file was saved! Thanks for using my password generator!\n Would you like to exit the program?")
    if answer:
        root.destroy()


def save_file():
    with open('created_passwords.txt', 'w', encoding='utf-8') as file:
        for item in passwords:
            file.write("%s\n" % item)
        print("File saved!")
        thank_you()


def single_pass_popup():
    def button_click():
        print(user_input.get())
        pass_len = int(user_input.get())
        answer = tkinter.messagebox.askyesno(master=window,
                                             message="Would you like your password to include punctuation marks?")
        ttk.Label(window, text="Note: Some sites don't allow punctuation marks on their passwords")
        if answer:
            print(generate_password(pass_len, use_punctuation=True))
            passwords.append(generate_password(pass_len, use_punctuation=True))
            save_file()
        else:
            print(generate_password(pass_len, use_punctuation=False))
            passwords.append(generate_password(pass_len, use_punctuation=True))
            save_file()

    window = Toplevel(root)
    window.grid()
    window.title("Character length")
    ttk.Label(window, text="How long (in characters) would you like your password to be?").grid(column=2, row=1)
    user_input = ttk.Entry(window)
    user_input.grid(column=2, row=2)
    ttk.Label(window, text="Please insert a numerical value").grid(column=2, row=3)
    ttk.Button(window, text="Accept", command=button_click).grid(column=2, row=4)


mainframe = ttk.Frame(root, padding="3 3 12 12")  # Look up what that padding does
# noinspection PyTypeChecker
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Welcome!").grid(column=2, row=1)
ttk.Button(mainframe, text="Generate a single password", command=single_pass_popup).grid(column=2, row=2)
ttk.Button(mainframe, text="Generate multiple passwords").grid(column=2, row=3, sticky=S)

root.mainloop()  # So the window actually stays open until the user closes it
