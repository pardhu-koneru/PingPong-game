from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
    def move(self):
        x = self.xcor()+self.x_move
        y = self.ycor()+ self.y_move
        self.goto(x,y)

    def bounce_back(self):
        self.y_move *= -1

    def bounce_up(self):
        self.x_move *= -1

    def when_home(self):
        self.x_move *= -1
