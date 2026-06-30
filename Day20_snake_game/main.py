from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

""" Remember that the size if each turtle is 20px X 20px"""
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
'''Turned off the tracer so it does not produce the animation for everything. That way I can control when the screen needs to be update 
   to get the animation I need. The reason for that is, I avoid snail animation for the snake where each of the squares move one by one
   The way to refresh the screen when I need it, is the screen.update() function.
'''
screen.tracer(0) 


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update() # After each run the screen gets update. 
    time.sleep(0.1) # Slowing things down. after all forwading for each iteration in the game, we pause the screen for a second. Each time the for loop runs
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with self
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False
        
        




screen.exitonclick()