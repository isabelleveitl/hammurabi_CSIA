import tkinter as tk
from tkinter import *

class View:

    def __init__(self):
        window = tk.Tk()
        window.title("Hammurabi")
        window.resizable(False, False)
        Label(window,text="Hammurabi",fg = "dark green",font = "Helvetica 20 bold italic").grid(row=1, pady=5, padx=5)
        Label(window,text="The classic game of strategy and resource allocation",fg = "dark green",font = "Helvetica 18 bold italic").grid(row=2, pady=5, padx=5)
        Label(window,text="Hammurabi: I beg to report to you,",font = "Helvetica 16").grid(row=3, pady=5, padx=5)

        Label(window, text="How many acres do you wish to buy or sell?").grid(row=5, pady=5, padx=5)
        input1 = Text(master=window, width=30, height=1, wrap='word')
        input1.grid(row=5, column=1, columnspan=6, pady=10, padx=5)
        Label(window, text="How many bushels do you wish to feed your people?").grid(row=6, pady=5, padx=5)
        input2 = Text(master=window, width=30, height=1, wrap='word')
        input2.grid(row=6, column=1, columnspan=6, pady=10, padx=5)
        Label(window, text="How many acres do you wish to plant with seed? ").grid(row=7, pady=5, padx=5)
        input3 = Text(master=window, width=30, height=1, wrap='word')
        input3.grid(row=7, column=1, columnspan=6, pady=10, padx=5)

        btn = tk.Button(window,text="Make it so!" ,bg="red", fg="white")
        btn.grid(row=8, pady=5, padx=5)

    window.mainloop()