import time
from turtle import Turtle,Screen
from Create_Paddle import Paddle
from ScoreBoard import ScoreBoard
from Ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.listen()
# screen.tracer(0)# this should be written in starting stage of code

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
r_paddle.speed("fast")
l_paddle.speed("fast")
ball = Ball()
score = ScoreBoard()
ball.penup()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
lag = 0.5
game_on = True
while game_on:
    screen.update()
    time.sleep(lag)
    ball.move()

    #DETECT WALL COLLISION
    if ball.ycor() > 280:
        ball.bounce_back()
    if ball.ycor() < -280:
        ball.bounce_back()

    #DETECT PADDLE COLLISION
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_up()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_up()

    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        score.update_right_score()
        ball.goto(0, 0)
        ball.when_home()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        score.update_left_score()
        ball.goto(0, 0)
        ball.when_home()
    lag *= 0.5
    if score.score_right == 10 or score.score_left ==10 :
        game_on = False



screen.exitonclick()