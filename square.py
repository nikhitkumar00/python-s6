from turtle import Turtle
t = Turtle()
t.up()
t.goto(100,100)
t.down()
t.setheading(270)
for i in range(4):
    t.forward(200)
    t.right(90)