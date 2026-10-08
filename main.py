import turtle
from math import dist
from random import randint

t = turtle.Turtle()
wn = turtle.Screen()
wn.listen()
wn.onkey(wn.bye, "Return")

w, h = 1000, 1000

wn.setup(width=w, height=h)
t.speed(0)
wn.tracer(0)


side = 3
amount = 10000
size = w / 2
edge = True


angle = 360 / side


t.penup()
t.bk(w / 2)
if edge:
    t.penup()
else:
    t.pendown()
cords = []
for _ in range(side):
    cords.append((t.xcor(), t.ycor()))
    t.fd(size)
    t.rt(angle)

t.penup()

for i in range(amount):
    vertex = randint(0, side - 1)
    d = dist((t.xcor(), t.ycor()), cords[vertex])
    t.setheading(t.towards(cords[vertex]))
    t.fd(d / 2)
    t.pendown()
    t.circle(1)
    t.penup()
    if i % 100 == 0:
        wn.update()

wn.update()
wn.mainloop()
