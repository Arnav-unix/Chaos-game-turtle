# user entered variables
side = int(input("Sides: "))
amount = int(input("Amount: "))
opr = "d " + input("e.g Distance / 2\nDistance ")
suf = int(input(f"How fast do you want it to be (1 to {amount})\n>>> "))

# Importing
import turtle
from math import dist
from random import randint

# Setting up turtle and screen
t = turtle.Turtle()
t.color("green")
t.pencolor("black")
t.shape("turtle")
t.pensize(1)
wn = turtle.Screen()
wn.listen()
wn.onkey(wn.bye, "Return")
w, h = 1000, 1000
wn.setup(width=w, height=h)
t.speed(0)
wn.tracer(0)

# Other variables
size = w / side * 1.5
edge = False
angle = 360 / side


# Getting the shape (vertices)
t.penup()
t.bk(size / 2)
if edge:
    t.pendown()
else:
    t.penup()
cords = []
for _ in range(side):
    cords.append((t.xcor(), t.ycor()))
    t.fd(size)
    t.lt(angle)
t.penup()


# Drawing the shape
for i in range(amount):
    vertex = randint(0, side - 1)
    d = dist((t.xcor(), t.ycor()), cords[vertex])
    t.setheading(t.towards(cords[vertex]))
    t.fd(eval(opr))
    t.pendown()
    t.circle(1)
    t.penup()
    # Screen updating frequency
    if i % suf == 0:
        wn.update()

# Celebration
t.goto(0, -h / 4)
t.setheading(90)
print("Done")
wn.tracer(1)
while True:
    t.rt(1)
# wn.update()
# wn.mainloop()
