from turtle import Turtle, Screen

FONT = ("Arial", 16, "normal")

def isCollision(t1, t2):
    return t1.distance(t2) < 15

# set up screen
screen = Screen()
screen.bgcolor("gray")
screen.title("Pong by Mahmoud Abdellatif")

# set up border
border_pen = Turtle(visible=False)
border_pen.speed('fastest')
border_pen.color('white')
border_pen.pensize(3)

border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()

for _ in range(4):
    border_pen.forward(600)
    border_pen.left(90)

# set score to 0
score = 0

# set time to zero
seconds = 0

# Draw score
score_pen = Turtle(visible=False)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 310)

score_pen.write("Score {}".format(score), False, align="left", font=FONT)

# Draw timer
time_pen = Turtle(visible=False)
time_pen.color("white")
time_pen.penup()
time_pen.setposition(260, 310)

time_pen.write("Time {}".format(int(seconds)), False, align="left", font=FONT)

# create the player turtle
player = Turtle("square", visible=False)
player.shapesize(0.5, 3)
player.speed('fastest')
player.setheading(90)
player.color("blue")
player.penup()

player.setposition(-280, -250)  # (x,y)
player.showturtle()

playerspeed = 15

# create the AIplayer turtle
AIplayer = Turtle("square", visible=False)
AIplayer.shapesize(0.5, 3)
AIplayer.speed('fastest')
AIplayer.setheading(90)
AIplayer.color("black")
AIplayer.penup()

AIplayer.setposition(280, 250)  # (x,y)
AIplayer.showturtle()

AIplayerspeed = 15

# create the pong
pong = Turtle("circle", visible=False)
pong.shapesize(0.5, 0.5)
pong.speed('fast')
pong.color("red")
pong.penup()

pong.sety(265)
pong.showturtle()

pongspeed = 15
pong_dx, pong_dy = 5, -5

# Move player up and down
def move_up():
    player.forward(playerspeed)

    y = player.ycor()

    if y > 265:
        y = 260
        player.sety(y)

    screen.update()

def move_down():
    player.backward(playerspeed)

    y = player.ycor()

    if y < -265:
        y = -260
        player.sety(y)

    screen.update()

# keyboard bindings
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.listen()

# main game loop
def move():
    global pong_dx, pong_dy, AIplayerspeed, seconds, score

    # move pong ball
    x, y = pong.position()
    x += pong_dx
    y += pong_dy
    pong.setposition(x, y)

    if isCollision(pong, player): # collision pong and player
        pong_dx *= -1
        # Update the score
        score += 10
        score_pen.undo()
        score_pen.write("Score: {}".format(score), align="left", font=FONT)
    elif isCollision(pong, AIplayer):  # collision pong and AIplayer
        pong_dx *= -1
    elif y < -300 or y > 300:  # check for bounce and redirect it
        pong_dy *= -1
    elif x > 300:
        pong_dx *= -1
    elif x < -300:
        print("Game Over")
        screen.bye()
        return

    # move AI paddle (might speed up pong movement)
    AIplayer.forward(AIplayerspeed)

    y = AIplayer.ycor()

    if y < -250 or y > 250:
        AIplayerspeed *= -1

    # display timer
    seconds += 0.05
    time_pen.undo()
    time_pen.write("Time: {}".format(int(seconds)), False, align="Left", font=FONT)
    screen.ontimer(move, 50)

    screen.update()

screen.tracer(False)
move()
screen.mainloop()
