import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Create the objects and can only go up
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1) #Every 0.1 second the screen updates
    screen.update()

    #And that create and move cars
    carmanager.create_car()
    carmanager.car_move()

    #Detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    #Detect successful cross
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()    
        scoreboard.level_up_board()




screen.exitonclick()
