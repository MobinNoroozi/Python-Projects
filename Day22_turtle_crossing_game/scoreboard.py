from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(-280, 270)
        self.score = 0
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align = "left", font =(FONT))

    def level_up_board(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align= "center", font= FONT)
