from turtle import Turtle 

class Scoreboard(Turtle):

   
#This is also a turtle
    def __init__(self):
        super().__init__() 
        self.score = 0 #initial score is 0
       
        with open("data.txt") as data: #Opens the data.txt that holds the all time high score
            self.highest_score = int(data.read()) #Reads that data and saves it
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard() #Display the score 
        
        
    def update_scoreboard(self):    
        self.clear() #Clear before getting data
       #Displays the score
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align="center", font=("Arial", 24, "normal"))

   
    def reset(self):
       #When reseting, it gets the highest score, it saves it
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0 #Then it reset the score 
        self.update_scoreboard() #And then it updates
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
