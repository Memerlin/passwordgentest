from tkinter import *
from tkinter import ttk
from passwordgen import generate_password
# This is built with tkinter version 8.6.12
root = Tk()
root.title("Jim's password generator!")
mainframe = ttk.Frame(root, padding="3 3 12 12")  # Look up what that padding does
# noinspection PyTypeChecker
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Welcome!").grid(column=2, row=1)
ttk.Button(mainframe, text="Generate a single password").grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="Generate multiple passwords").grid(column=3, row=2, sticky=E)
root.mainloop()  # So the window actually stays open until the user closes it
