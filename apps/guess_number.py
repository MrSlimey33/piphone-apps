
import tkinter as tk
import random

def launch(frame):
    frame.destroy()
    frame = tk.Frame(frame.master, bg="orange")
    frame.place(relwidth=1, relheight=1)
    tk.Label(frame,text="Guess the Number",bg="orange",fg="white",font=("Arial",16)).pack()
    number = random.randint(1,50)
    guess_var = tk.StringVar()
    tk.Entry(frame,textvariable=guess_var).pack()
    result = tk.Label(frame,text="",bg="orange",fg="white")
    result.pack()
    def check():
        try:
            g = int(guess_var.get())
            if g==number:
                result.config(text="Correct!")
            elif g<number:
                result.config(text="Too low")
            else:
                result.config(text="Too high")
        except:
            result.config(text="Enter a number")
    tk.Button(frame,text="Guess",command=check,bg="darkgray").pack()
    tk.Button(frame,text="?? Home",command=lambda:frame.destroy(),bg="darkgray").pack(side="bottom",fill="x")
