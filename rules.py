from turtle import Turtle, Screen
import csv
import pandas


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 0
        self.scoreguess = "Guess the state"

    def Go(self, x, ye, state):
        self.goto(x, ye)
        self.write(f"{state}", align="center", font=("Ariel", 8, "bold"))

    def Score(self):
        self.score += 1
        self.scoreguess = f"{self.score}/50 States Correct"

    def Ask(self):

        self.stet = self.screen.textinput(title=f"{self.scoreguess}", prompt="Insert state name:").title()



