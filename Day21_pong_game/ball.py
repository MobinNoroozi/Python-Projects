from turtle import Turtle

class Ball(Turtle):
    #Setting the properties
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10 #Start moving right and down by 10 pixels
        self.y_move = 10
        self.move_speed = 0.1 #Speed to start with


    def move(self):
        #Moves the ball by 10 pixels
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)


    def bounce_y(self):
        # When the ball hits the top or bottom of the screen bounces back
        self.y_move *= -1

    # When the ball hits the paddle it boounces back, and its speed gets faster
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    #Reset the speed and position and this time it goes the other way
    def reset_position(self):
        self.goto(0, 0 )
        self.move_speed = 0.1
        self.x_move *= -1

