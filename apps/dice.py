
import tkinter as tk
import random

def launch(frame):
    frame.destroy()
    frame = tk.Frame(frame.master, bg="brown")
    frame.place(relwidth=1, relheight=1)
    tk.Label(frame,text="Dice Roller",bg="brown",fg="white",font=("Arial",16)).pack()
    result = tk.Label(frame,text="",bg="brown",fg="white",font=("Arial",16))
    result.pack()
    def roll():
        result.config(text=str(random.randint(1,6)))
    tk.Button(frame,text="Roll Dice",command=roll,bg="darkgray").pack()
    tk.Button(frame,text="?? Home",command=lambda:frame.destroy(),bg="darkgray").pack(side="bottom",fill="x")
