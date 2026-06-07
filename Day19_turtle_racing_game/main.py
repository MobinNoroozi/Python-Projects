from turtle import Turtle, Screen
import random

is_race_on = False

# Setting the screen
screen = Screen()
screen.setup(width=500, height=400)

# This allows the user to input. Technically an input in turtle module.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"] #List of colors for our turtles
y_positions = [-70, -40, -10, 20, 50, 80] # Different y position for each turtle
all_turtles = [] # List of all turtles which we will append them here later


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle") # For 6 turtles we create 6 turtles 
    new_turtle.color(colors[turtle_index]) # Each of them has a specific color, and we get that color from the colors list. To make it easy we get it from the index
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) # Each turtle goes to set x position, and a different y position so they can be on the same line
    all_turtles.append(new_turtle) # Append each turtle to the list


if user_bet: # If user has prompted, the race is on
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if (turtle.xcor() > 230): # If the turtle is at the end, the race is over
            is_race_on = False

            winning_color = turtle.pencolor() # Get the color of the turtle

            if winning_color == user_bet: # If user guessed the same, they win, otherwise they lose. 
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10) # If not at the end yet, get a random number between 0, 10
        turtle.forward(random_distance) # Make current turtle go forward by this amount









screen.exitonclick()