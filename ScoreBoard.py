from turtle import Turtle


# tim_left = Turtle()
# tim_right = Turtle()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.hideturtle()
        self.goto(-20, 270)
        self.write(f"{self.score_left}", False, "center", ("Arial", 20, "normal"))
        self.goto(20, 270)
        self.write(f"{self.score_right}", False, "center", ("Arial", 20, "normal"))

    def update_left_score(self):
        # self.clear()
        self.score_left += 1
        self.update_score()

    def update_right_score(self):
        # self.clear()
        self.score_right += 1

        self.update_score()
