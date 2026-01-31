
import tkinter as tk

def launch(frame):
    frame.destroy()
    frame = tk.Frame(frame.master, bg="blue")
    frame.place(relwidth=1, relheight=1)
    tk.Label(frame,text="Counter",bg="blue",fg="white",font=("Arial",16)).pack()
    count = tk.IntVar(value=0)
    lbl = tk.Label(frame,textvariable=count,bg="blue",fg="white",font=("Arial",16))
    lbl.pack()
    tk.Button(frame,text="+",command=lambda: count.set(count.get()+1),bg="darkgray").pack()
    tk.Button(frame,text="-",command=lambda: count.set(count.get()-1),bg="darkgray").pack()
    tk.Button(frame,text="?? Home",command=lambda:frame.destroy(),bg="darkgray").pack(side="bottom",fill="x")
