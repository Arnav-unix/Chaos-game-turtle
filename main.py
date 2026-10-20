# Importing
import turtle
import tkinter as tk
from math import dist
from random import randint


# Tkinter stuff

inp = tk.Tk()
inp.title("Input")
inp.geometry("200x300")

side = tk.IntVar(value=3)
opr = tk.StringVar(value="distance / 2")
amount = tk.IntVar(value=10000)
sur = tk.IntVar(value=100)
color = tk.StringVar(value="black")
bgcolor = tk.StringVar(value="white")

# Labels and Entries
sidelb = tk.Label(inp, text="Enter sides")
sidesp = tk.Spinbox(inp, from_=3, to=30, textvariable=side)
oprlb = tk.Label(inp, text="Enter operation")
opren = tk.Entry(inp, textvariable=opr)
amountlb = tk.Label(inp, text="Enter Amount of cycles")
amountsp = tk.Spinbox(inp, from_=1, to=30000, textvariable=amount)
surlb = tk.Label(inp, text="Enter screen update rate")
sursp = tk.Spinbox(inp, from_=1, to=1000, textvariable=sur)
colorlb = tk.Label(inp, text="Enter color")
coloren = tk.Entry(inp, textvariable=color)
bgcolorlb = tk.Label(inp, text="Enter Bgcolor")
bgcoloren = tk.Entry(inp, textvariable=bgcolor)


# Button


def ok():
    inp.destroy()


okbutton = tk.Button(inp, text="Ok", command=ok)

# Packing
sidelb.pack()
sidesp.pack()
oprlb.pack()
opren.pack()
amountlb.pack()
amountsp.pack()
surlb.pack()
sursp.pack()
colorlb.pack()
coloren.pack()
bgcolorlb.pack()
bgcoloren.pack()
okbutton.pack()

inp.mainloop()


# Setting up turtle and screen
t = turtle.Turtle()
t.color("green")
t.pencolor(color.get())
t.shape("turtle")
t.pensize(1)
wn = turtle.Screen()
wn.bgcolor(bgcolor.get())
w = wn.window_width()
h = wn.window_height()
wn.setup(width=1.0, height=1.0)
t.speed(0)
wn.tracer(0)

# Other variables
size = w / side.get() * 1.5
edge = False
angle = 360 / side.get()


# Getting the shape (vertices)
t.penup()
t.bk(size / 2)
if edge:
    t.pendown()
else:
    t.penup()
cords = []
for _ in range(side.get()):
    cords.append((t.xcor(), t.ycor()))
    t.fd(size)
    t.lt(angle)
t.penup()


# Drawing the shape
for i in range(amount.get()):
    vertex = randint(0, side.get() - 1)
    distance = dist((t.xcor(), t.ycor()), cords[vertex])
    t.setheading(t.towards(cords[vertex]))
    t.fd(eval(opr.get()))
    t.dot(2)
    # Screen updating frequency
    if i % sur.get() == 0:
        wn.update()

# Celebration
t.goto(0, -h / 4)
t.setheading(90)
print("Done")
wn.update()
wn.exitonclick()
