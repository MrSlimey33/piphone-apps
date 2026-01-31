def launch(root):
    import tkinter as tk
    tk.Label(root, text="Snake Game", font=("Arial",16), bg="black", fg="white").pack(expand=True, fill="both")
    tk.Button(root, text="🏠 Home", command=lambda: root.master.tkraise(), bg="darkgray").pack(side="bottom", fill="x")
