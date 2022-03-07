from turtle import *
import time
import random

def left():
    paddle.goto(paddle.pos()[0]-40, paddle.pos()[1])

def right():
    paddle.goto(paddle.pos()[0]+40, paddle.pos()[1])

def play():
    game_on = True
    text.clear()
    global x, y, count, record, blocks
    while game_on:
        time.sleep(0.01)
        screen.update()
        ball.goto(ball.xcor() + x, ball.ycor() + y)
        if ball.xcor() > 390 or ball.xcor() < - 390:
            x = -x
        if ball.ycor() > 390:
            y = -y
        if ball.distance(paddle) < 50 and ball.ycor() < -330:
            y = -y
        if ball.ycor() < -410:
            game_on = False
        for block in blocks:
            if ball.distance(block) < 50 and ball.ycor() > block.ycor() - 10 and ball.ycor() < block.ycor() + 10:
                y = -y
                block.goto(12000, 12000)
                count += 1
                score.clear()
                score.write(f"Score: {count}", False, "center", ("Arial", 24, "normal"))
    if count > record:
        record = count
        high_score.clear()
        high_score.write(f"Highest Score: {record}", False, "center", ("Arial", 24, "normal"))

    count = 0
    score.clear()
    score.write(f"Score: {count}", False, "center", ("Arial", 24, "normal"))
    x = 6
    y = 6
    paddle.goto(0, -350)
    ball.goto(0, -330)
    for block in blocks:
        block.goto(10000, 10000)
    blocks.clear()
    for x_cord in xcors:
        for y_cord in ycors:
            add_block(x_cord, y_cord)
    text.write(f"Press space to start game", False, "center", ("Arial", 24, "normal"))

def add_block(x_cord, y_cord):
    new_block = Turtle("square")
    new_block.shapesize(1, 4)
    new_block.penup()
    new_block.color(random.choice(color_list))
    new_block.goto(x_cord, y_cord)
    blocks.append(new_block)

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("---Breakout---")
tracer(0)

count = 0
score = Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(-150, 350)
score.write(f"Score: {count}", False, "center", ("Arial", 24, "normal"))

record = 0
high_score = Turtle()
high_score.color("red")
high_score.hideturtle()
high_score.penup()
high_score.goto(200, 350)
high_score.write(f"Highest Score: {record}", False, "center", ("Arial", 24, "normal"))


text = Turtle()
text.color("white")
text.hideturtle()
text.penup()
text.goto(0, 0)
text.write(f"Press space to start game", False, "center", ("Arial", 24, "normal"))

paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(1, 5)
paddle.penup()
paddle.goto(0, -350)

screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(play, "space")

ball = Turtle()
ball.shape("circle")
ball.shapesize(1, 1)
ball.color("white")
ball.penup()
ball.goto(0, -330)
x = 6
y = 6

blocks =[]
xcors = [-350, -250, -150, -50, 50, 150, 250, 350]
ycors = [280, 245, 210, 175, 140, 105]
color_list = ["violet", "blue", "green", "yellow", "orange", "red", "white", "purple"]
for x_cord in xcors:
    for y_cord in ycors:
        add_block(x_cord, y_cord)


screen.exitonclick()