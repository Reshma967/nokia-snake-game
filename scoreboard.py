from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score:{self.score}", align= "center" ,font=("Arial",23,"normal"))
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.write("Game Over", align="center", font=("Arial", 23, "normal"))

    def inc_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}", align="center", font=("Arial", 23, "normal"))