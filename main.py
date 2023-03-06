from turtle import Turtle, Screen
from Paddle import Paddles
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddles((350, 0))
r_paddle = Paddles((-350, 0))


screen.listen()
#for left paddle
screen.onkey(fun=l_paddle.go_up, key="Up")
screen.onkey(fun=l_paddle.go_down, key="Down")
#for right paddle
screen.onkey(fun=r_paddle.go_up, key="w")
screen.onkey(fun=r_paddle.go_down, key="s")


ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("BALL Collied with PAddle.")
        ball.bounce_x()
        

screen.exitonclick()
