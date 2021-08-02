import time
from turtle import Screen
from snake import snake
from food import food
from scoreboard import ScoreBoard

score_board = ScoreBoard()

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake()
food = food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snakes[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score_board.update()

    if snake.snakes[0].xcor() > 290 or snake.snakes[0].xcor() < -290 or snake.snakes[0].ycor() > 290 or snake.snakes[0].ycor() < -290:

        game_is_on = False
        score_board.game_over()

    for segments in snake.snakes[2:]:
         if snake.snakes[0].distance(segments) < 10:
            game_is_on = False
            score_board.game_over()



screen.exitonclick()