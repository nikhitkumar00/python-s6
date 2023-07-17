from turtle import Turtle
import time 
t = Turtle()
t.width(4)
t.color("black","red")
t.begin_fill()
for i in range (5):
    t.forward(300)
    t.left(144)
t.end_fill()
time.sleep(3)