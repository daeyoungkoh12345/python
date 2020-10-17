import turtle as t
import random as r

playing=True

def up():
    t.setheading(90)
    t.forward(5)
def down():
    t.setheading(270)
    t.forward(5)
def left():
    t.setheading(180)
    t.forward(5)
def right():
    t.setheading(0)
    t.forward(5)
def space():
    t.clear()
def play():
    if playing:
        t.ontimer(play,100)
    if t.distance(ts)<12:
        x=r.randint(-230,230)
        y=r.randint(-230,230)
        ts.goto(x,y)

t.setup(500,500)
t.bgcolor("black")
t.shape("triangle")
t.color("red")

#김세모 먹이
ts=t.Turtle()
ts.color("blue")
ts.shape("triangle")
ts.up()
ts.goto(-100,-150)


t.onkeypress(up,"Up")
t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.onkeypress(down,"Down")
t.onkeypress(space,"space")

t.listen()
play()


