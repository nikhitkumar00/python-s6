from turtle import Turtle
t= Turtle()
t.up()
t.goto(-100,100)
t.down()
t.fillcolor("red")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(144)
t.end_fill()