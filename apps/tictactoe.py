
import tkinter as tk

def launch(frame):
    frame.destroy()
    frame = tk.Frame(frame.master, bg="purple")
    frame.place(relwidth=1, relheight=1)
    tk.Label(frame,text="Tic-Tac-Toe",bg="purple",fg="white",font=("Arial",16)).pack()
    board = [""]*9
    buttons = []
    player = ["X"]
    def check_win():
        combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in combos:
            if board[a]==board[b]==board[c]!="" :
                tk.Label(frame,text=f"{board[a]} Wins!",bg="purple",fg="yellow").pack()
                return True
        if "" not in board:
            tk.Label(frame,text="Draw!",bg="purple",fg="yellow").pack()
            return True
        return False
    def press(i):
        if board[i]=="":
            board[i]=player[0]
            buttons[i].config(text=player[0])
            player[0] = "O" if player[0]=="X" else "X"
            check_win()
    grid_frame = tk.Frame(frame,bg="purple")
    grid_frame.pack()
    for i in range(9):
        btn = tk.Button(grid_frame,text="",width=5,height=2,font=("Arial",16),command=lambda i=i:press(i))
        btn.grid(row=i//3,column=i%3)
        buttons.append(btn)
    tk.Button(frame,text="?? Home",command=lambda:frame.destroy(),bg="darkgray").pack(side="bottom",fill="x")
