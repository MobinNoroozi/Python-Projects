import turtle
import random
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255) # Allows us to use rgb colors in the turtle module

color_list = [] 

colors = colorgram.extract("painting.jpg", 100) # part of the colorgram that extract up to 100 colors from the image

# This extract rgb from each color in the colors, and appends it to the color list. Which is a list of tuples representing rgb respectively
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)


# Choosing numbers of columns and rows to be drawn
num_columns = 14
num_rows = 13


tim = Turtle()
screen = Screen()



def reset_heading():
    tim.penup()
    tim.setheading(90) #Go up 50
    tim.forward(50)
    tim.setheading(180) #Toward 180 degrees
    #Will take back to where we started
    for i in range(num_columns):
        tim.forward(50) 


def draw_a_row():
    tim.setheading(0)
    for i in range(num_columns):
        # Size 18, and a random rgb tuple is passed into the dot, which draws a dot
        tim.dot(18, random.choice(color_list))
        tim.penup() # We do not need to see the line drawing 
        tim.forward(50)
        tim.pendown()

def set_initial():
    # It takes you to the corner and gets ready to draw
    tim.penup()
    tim.setheading(220) #225 degrees
    tim.forward(440) #distance form center

def draw_num_of_rows(rows):
    # Draws the requested number of rows
    for i in range(rows):
        draw_a_row()
        reset_heading()
  
        
tim.hideturtle()
tim.speed("fastest")
set_initial()
draw_num_of_rows(num_rows)



screen.exitonclick()