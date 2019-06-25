import tkinter as tk
from tkinter import *

class View:

    def __init__(self, city):
        self.city = city
        self.window = tk.Tk()
        self.window.title("Hammurabi")
        self.window.resizable(False, False)
        introduction_text = self.setText()
        self.listener = None

        Label(self.window, text="Hammurabi", fg="dark green", font="Helvetica 20 bold italic").grid(row=1, pady=5, padx=5)
        Label(self.window, text="The classic game of strategy and resource allocation", fg="dark green",
              font="Helvetica 18 bold italic").grid(row=2, pady=5, padx=5)
        Label(self.window, text="Hammurabi: I beg to report to you,", font="Helvetica 16").grid(row=3, pady=5, padx=5)
        Label(self.window, text=introduction_text, font="Helvetica 16").grid(row=4, pady=5, padx=5)
        Label(self.window, text="How many acres do you wish to buy or sell?").grid(row=5, pady=5, padx=5)
        self.input1 = Text(master=self.window, width=30, height=1, wrap='word')
        self.input1.grid(row=5, column=1, columnspan=6, pady=10, padx=5)
        Label(self.window, text="How many bushels do you wish to feed your people?").grid(row=6, pady=5, padx=5)
        self.input2 = Text(master=self.window, width=30, height=1, wrap='word')
        self.input2.grid(row=6, column=1, columnspan=6, pady=10, padx=5)
        Label(self.window, text="How many acres do you wish to plant with seed? ").grid(row=7, pady=5, padx=5)
        self.input3 = Text(master=self.window, width=30, height=1, wrap='word')
        self.input3.grid(row=7, column=1, columnspan=6, pady=10, padx=5)

        self.btn = tk.Button(self.window, text="Make it so!", bg="red", fg="white", command=lambda: self.change())
        self.btn.grid(row=8, pady=5, padx=5)

        self.btn2 = tk.Button(self.window, text="New Game", bg="red", fg="white", command=lambda: self.change2())
        self.btn2.grid(row=8, column=1, columnspan=6, pady=5, padx=5)


    def setText(self):
        print(self.city.city_name)
        m = 2
        introduction_text = 'In Year ' + str(self.city.year) + ', ' + str(self.city.starved) + ' people starved. ' + str(self.city.death_by_illness) + ' people where ill. \n' \
                            + str(self.city.immigrants) + ' people came to the city. \n' \
                            'The city population is now ' + str(int(self.city.population)) + '. \n' \
                            'The city now owns ' + str(int(self.city.acres)) + ' acres.\n' \
                            'You harvested ' + str(int(self.city.harvest)) + ' bushels per acre.\n' \
                            'Rats ate ' + str(int(self.city.loss_by_rats)) + ' bushels.\n' \
                            'You now have ' + str(int(self.city.bushel)) + ' bushels in store.\n' \
                            'Land is trading at ' + str(self.city.price) + ' bushels per acre.'

        return introduction_text

    def set_listener(self, listener):
        self.listener = listener

    def change(self):
        if self.listener:
            print('call listener')
            acres = self.input1.get("1.0", END)
            food = self.input2.get("1.0", END)
            plant = self.input3.get("1.0", END)

            self.listener(acres, food, plant)

    def set_listener2(self, listener2):
        self.listener2 = listener2

    def change2(self):
        if self.listener2:
            print('call listener2')
            self.listener2()

    def click_handler_btn2(event):
        print('button2')

    def show(self):
        self.window.mainloop()

    def setInfo(self):
        Label(self.window, text=self.setText(), font="Helvetica 16").grid(row=4, pady=5, padx=5)
        self.window.update()
        self.window.update_idletasks()


