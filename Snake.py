# imports
import turtle
import time
import random

# Functions
def move():

    for i in range (len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def randomFood():
    x = 20 * random.randint(-15, 14)
    y = 20 * random.randint(-14, 15)
    food.goto (x + 5, y - 5)

# Module
window = turtle.Screen()
window.title("Snake")
window.bgcolor("black")
window.setup(width = 610, height = 610)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(5,-5)
head.direction = "stop"

body = []
body.append(head)

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
randomFood()

#Keyboard

window.listen()

window.onkeypress(up, "w")
window.onkeypress(up, "Up")

window.onkeypress(down, "s")
window.onkeypress(down, "Down")

window.onkeypress(left, "a")
window.onkeypress(left, "Left")

window.onkeypress(right, "d")
window.onkeypress(right, "Right")


# Main game loop
while True:
    window.update()

    if head.distance(food) < 20:

        randomFood()

        # Add segment
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("white")
        segment.penup()
        body.append(segment)

    if head.xcor() <= -300 or head.xcor() >= 300 or head.ycor() <= -300 or head.ycor() >= 315:       
        time.sleep(2)
        for i in body:
            i.goto(1000,1000)
        head.goto(5,-5)
        randomFood()
        head.direction == "stop"
        body = [head]
    
    for i in range (1, len(body)):
        if head.distance(body[i]) < 20:
            time.sleep(2)
            for i in body:
                i.goto(1000,1000)
            head.goto(5,-5)
            randomFood()
            head.direction == "stop"
            body = [head]

    move()

    time.sleep(0.11)


window.mainloop()
