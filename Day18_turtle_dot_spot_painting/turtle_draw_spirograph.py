from turtle import Turtle, Screen
import random

import turtle

tim = Turtle()
screen = Screen()
tim.speed("fastest")
turtle.colormode(255) # Allows us to use rgb to add colors


# Returns a new tuple that is a random rgb
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    new_color = (r, g, b)
    return new_color



def draw(shift):
    nums = int((360/shift)) #Shift is the shift in degrees. This produces the number of circles needed. 
    for i in range(0, nums):
        tim.color(random_color())
        tim.circle(100) #Size of the circle
        new_heading = tim.heading() + shift
        tim.setheading(new_heading)


draw(5) 

    









screen.exitonclick()
