import turtle
import time
import random

D = 0.1    # to delay loop by 0.1 seconds

score = 0
high_score = 0


# for screen:
screen = turtle.Screen()
screen.title("SNAKE by Mihlayokuphela")
screen.bgcolor("blue")
screen.setup(width=700, height=700)
screen.tracer(0)   # turns off screen updates

# for snake head
head = turtle.Turtle()
head.speed(0) # the speed of its animation not its movement
head.shape("square")
head.color("red")
head.penup() # to stop turtle from drawing anything for now
head.goto(0, 0) # to put it at the centre of screen
head.direction = "stop"

# food

food = turtle.Turtle()
food.speed(0) # the speed of its animation not its movement
food.shape("circle")
food.color("grey")
food.penup() # to stop turtle from drawing anything for now
food.goto(0, 220)

# Initial Score

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("score = 0, High score = 0", align = "center", font = ("Courier", 24,"normal"))







# BODY

body = []


# functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        up = head.ycor() # to move to y cordinates
        head.sety(up +20) # move upwards by 20


    if head.direction == "down":
        down = head.ycor() # to move to y cordinates
        head.sety(down - 20) # move upwards by 20


    if head.direction == "left":
        left = head.xcor() # to move to y cordinates
        head.setx(left - 20) # move upwards by 20


    if head.direction == "right":
        right = head.xcor() # to move to y cordinates
        head.setx(right + 20) # move upwards by 20


# keyboard bindings
screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"d")



# main game loop
while True:
    screen.update()

    #check if snake colliding with boarder
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in body:  # to hide previous body segments if player crashes
            segment.goto(1000, 1000)

        body.clear() # to clear body list

        # reset score
        score = 0
        pen.clear()
        pen.write("Score:{} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:  # to check if head is touching food
        x = random.randint(-340, 340)
        y = random. randint(-340, 340)
        food.goto(x, y)

        # add body part
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("black")
        new_part.penup()
        body.append(new_part)

# increase score
    score = score + 5
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write("Score: {} High score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))


  # move body segments from last to 2nd last segment towards head
    for index in range(len(body) -1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

# move the segment immediately after head


    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    # check if theres body collision
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in body:  # to hide previous body segments if player crashes
                segment.goto(1000, 1000)

            body.clear()





    time.sleep(D) # delay by D

screen.mainloop()
