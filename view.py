import tkinter as tk
from tkinter import *
import controller as c


class View:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hammurabi")
        self.window.resizable(False, False)
        Label(self.window, text="Hammurabi", fg="dark green", font="Helvetica 20 bold italic").grid(row=1, pady=5,
                                                                                                    padx=5)
        Label(self.window, text="The classic game of strategy and resource allocation", fg="dark green",
              font="Helvetica 18 bold italic").grid(row=2, pady=5, padx=5)
        Label(self.window, text="Hammurabi: I beg to report to you,", font="Helvetica 16").grid(row=3, pady=5, padx=5)

        Label(self.window, text="How many acres do you wish to buy or sell?").grid(row=5, pady=5, padx=5)
        self.input1 = Text(master=self.window, width=30, height=1, wrap='word')
        self.input1.grid(row=5, column=1, columnspan=6, pady=10, padx=5)
        Label(self.window, text="How many bushels do you wish to feed your people?").grid(row=6, pady=5, padx=5)
        self.input2 = Text(master=self.window, width=30, height=1, wrap='word')
        self.input2.grid(row=6, column=1, columnspan=6, pady=10, padx=5)
        Label(self.window, text="How many acres do you wish to plant with seed? ").grid(row=7, pady=5, padx=5)
        self.input3 = Text(master=self.window, width=30, height=1, wrap='word')
        self.input3.grid(row=7, column=1, columnspan=6, pady=10, padx=5)

        self.btn = tk.Button(self.window, text="Make it so!", bg="red", fg="white", command=self.click_handler_btn)
        self.btn.grid(row=8, pady=5, padx=5)

        self.btn2 = tk.Button(self.window, text="New Game", bg="red", fg="white", command=self.click_handler_btn2)
        self.btn2.grid(row=8, column=1, columnspan=6, pady=5, padx=5)

    def click_handler_btn(event):
        print('button1')
        acres = event.input1.get("1.0", END)
        food = event.input2.get("1.0", END)
        plant = event.input3.get("1.0", END)
        c.update_city(acres, food, plant)

    def click_handler_btn2(event):
        print('button2')
        c.new_game()

    def show(self):
        self.window.mainloop()
