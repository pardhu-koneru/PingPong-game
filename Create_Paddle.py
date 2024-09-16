from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,position_x,position_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # THIS STRECHES THE WIDTH 5 TIMES AND LENGTH 1 TIME
        self.penup()
        self.goto(position_x,position_y)

    def go_up(self):
        if self.ycor() < 270:
            self.speed("fast")
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -270:
            self.speed("fast")
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)



