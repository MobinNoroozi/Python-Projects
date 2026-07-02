from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcord):
        #Setting the properties of the paddle
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.penup()
        self.xcord = xcord
        self.goto(self.xcord, 0)


    def go_up(self):
        #Moves by 20 pixels
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
