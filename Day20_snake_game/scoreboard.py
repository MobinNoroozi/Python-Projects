from turtle import Turtle 

class Scoreboard(Turtle):

   

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):    
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()