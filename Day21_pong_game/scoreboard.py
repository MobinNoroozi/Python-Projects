from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        #Setting the properties of scoreboeard which are 2 turtle objects
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        #Clear and print both of the turtles
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align= "center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align= "center", font=("Courier", 80, "normal"))


    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()
