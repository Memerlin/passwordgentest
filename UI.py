from tkinter import *
from tkinter import ttk
from passwordgen import generate_password

# This is built with tkinter version 8.6.12
root = Tk()
root.title("Jim's password generator!")
n = []
pass_length = []
pass_amount = []


def create_new_window():
    window = Toplevel(root)
    window.grid()
    window.title("Character length")
    ttk.Label(window, text="How long would you like your password to be?").pack()
    entry_window = ttk.Entry(window).pack()
    ttk.Label(window, text="Please insert a numerical value").pack()
    ttk.Button(window, text="Accept").pack()
    entry_window = entry_window.get()


mainframe = ttk.Frame(root, padding="3 3 12 12")  # Look up what that padding does
# noinspection PyTypeChecker
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Welcome!").grid(column=2, row=1)
ttk.Button(mainframe, text="Generate a single password", command=create_new_window).grid(column=2, row=2)
ttk.Button(mainframe, text="Generate multiple passwords").grid(column=2, row=3, sticky=S)

root.mainloop()  # So the window actually stays open until the user closes it
