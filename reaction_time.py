# import time
from tkinter import *
from time import *

from random import randint

root = Tk()
root.title("Reaction time")
global start
start = 0
global stop
stop = 0


def red_square():
    red_button.grid(row=1, column=1)



def green_square():
    global start
    red_button.config(bg='red')
    green_button.after(randint(1000, 6000))
    red_button.grid_remove()
    green_button.grid(row=1, column=1)
    start = time()
    print("inside green square water function")




def reaction_time():
    global start
    global stop
    stop = time()
    final_time = stop-start
    print(final_time)


red_button = Button(root, text="Red", bg='red',activebackground="red", padx=152, pady=152, command=lambda: green_square())
green_button = Button(root, text="green", bg='green', padx=150, pady=150, command=lambda: reaction_time())

red_square()
root.mainloop()