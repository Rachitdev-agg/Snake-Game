from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))
    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 14, "normal"))