from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from threading import Thread
from time import sleep
import sys
import keyboard


def run(*args):
    global my_timer
    my_timer = 5


def onkeypress(*args):
    global my_timer
    my_timer = 5
    timer = True
    while timer:
        sleep(1)
        my_timer -= 1
        entry_comp.bind('<KeyPress>', run)
        if my_timer == 0:
            timer = False
    entry_comp.delete("1.0", END)
    messagebox.showinfo(message="Nice work, Try harder.")
    sys.exit()


# ______ Root Setup ______

window = Tk()
window.title("Joshpydevops Speed Typing Test")
window.config(pady=50, padx=50, background="#222123")

label = Label(text="Joshpydevops Blocks Writer's Block", padding=10, font=("Arial", 25), foreground="crimson",
              background="#222123")
label.grid(column=0, row=1)

info = Label(
    text="don't stop typing or all progress will be deleted. You have 7 seconds.",
    padding=10, font=("Arial", 10, "italic"), wraplength=450, background="#222123", foreground="#eee3de")
info.grid(column=0, row=2)

# _______________ Text ______________________
x = 0
entry_comp = Text(height=15, width=90, wrap="word", background="#222123", foreground="#eee3de", font=('calibri', 10, 'normal'), padx=15, pady=15)
entry_comp.configure(insertbackground='white')
entry_comp.focus()
entry_comp.grid(column=0, row=4)

entry_comp.bind('<KeyPress>', Thread(target=onkeypress).start())

# window.bind('<KeyPress>', onkeypress)


window.mainloop()
