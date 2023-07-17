import turtle
import random

# Set up the turtle canvas
canvas = turtle.Screen()
canvas.bgcolor("#000000")
canvas.title("Firework")

# Define the turtle function
def draw_firework(t, x, y, color):
    # Set the turtle's properties
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)

    # Draw the explosion
    for i in range(25):
        t.begin_fill()
        t.circle(5*i)
        t.end_fill()

    # Draw the tail
    t.pensize(3)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(90)
    t.forward(100)

# Create the turtle
firework = turtle.Turtle()
firework.shape("turtle")
firework.speed(0)
firework.hideturtle()

# Draw the firework
draw_firework(firework, 0, 0, "#ffffff")

# Create multiple fireworks
for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"])
    draw_firework(firework, x, y, color)

# Exit on click
canvas.exitonclick()
