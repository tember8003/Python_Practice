import time
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,598)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake=Snake()
food =Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #음식과 부딪혔다면?
    if snake.head.distance(food)<18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #벽과 부딪혔다면?
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>298 or snake.head.ycor()<-298:
        scoreboard.game_over()
        game_is_on=False

    #꼬리와 부딪혔다면?
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()