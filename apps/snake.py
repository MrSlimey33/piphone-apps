
import tkinter as tk
import random

def launch(frame):
    frame.destroy()
    frame = tk.Frame(frame.master, bg="green")
    frame.place(relwidth=1, relheight=1)
    tk.Label(frame, text="Snake", bg="green", fg="white", font=("Arial",16)).pack()
    canvas = tk.Canvas(frame, width=300, height=300, bg="black")
    canvas.pack()
    square_size = 20
    snake = [[0,0]]
    direction = [square_size,0]
    food = [100,100]
    food_rect = canvas.create_rectangle(food[0],food[1],food[0]+square_size,food[1]+square_size,fill="red")

    def move():
        head = [snake[-1][0]+direction[0], snake[-1][1]+direction[1]]
        snake.append(head)
        snake.pop(0)
        canvas.delete("snake")
        for s in snake:
            canvas.create_rectangle(s[0],s[1],s[0]+square_size,s[1]+square_size,fill="white",tag="snake")
        if head==food:
            snake.append(food[:])
            new_food = [random.randint(0,14)*square_size, random.randint(0,14)*square_size]
            food[0],food[1] = new_food
            canvas.coords(food_rect, food[0],food[1],food[0]+square_size,food[1]+square_size)
        frame.after(200,move)

    def key(event):
        nonlocal direction
        if event.keysym=="Up" and direction[1]==0: direction=[0,-square_size]
        if event.keysym=="Down" and direction[1]==0: direction=[0,square_size]
        if event.keysym=="Left" and direction[0]==0: direction=[-square_size,0]
        if event.keysym=="Right" and direction[0]==0: direction=[square_size,0]

    frame.bind_all("<Key>", key)
    move()
