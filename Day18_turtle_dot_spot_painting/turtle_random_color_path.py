import random

import turtle as t #import the turtle as t because it is easier to type
from turtle import Screen
screen = Screen() 

tim = t.Turtle() # Our turtle object

# Creating a screen object and set it to exit on click

t.colormode(255) # So I can use RGB in terms of ranges

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    new_color = (r, g, b)
    return new_color



# List of possible angles
angles = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for i in range(0,500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angles))
    





screen.exitonclick()
