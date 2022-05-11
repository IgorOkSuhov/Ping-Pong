import turtle
from random import choice,randint
# Creating a playing field

window = turtle.Screen()
window.title('The Game of year Edition: PING-PONG GAME =)')
window.setup(width=1.0,height=1.0)
window.bgcolor('black')
window.tracer(1)

# Denote the boundary of the field

border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

# Create middle

border.goto(0,300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

#Create first rocket

rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_len=1,stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450,0)

#creation of management rocket
#'you can managment rocket A from keyboard, up(W) and down(S)'

def move_up():
    y = rocket_a.ycor() + 30
    if y > 250:
        y = 250
    rocket_a.sety(y)
def move_down():
    y = rocket_a.ycor() - 30
    if y < -250:
        y = -250
    rocket_a.sety(y)

# create second rocket

rocket_b = turtle.Turtle()
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_len=1,stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450,0)
#Okey, too play second rocket press Up and Down at you keyboard
def move_up_b():
    y = rocket_b.ycor() + 30
    if y > 250:
        y = 250
    rocket_b.sety(y)
def move_down_b():
    y = rocket_b.ycor() - 30
    if y < -250:
        y = -250
    rocket_b.sety(y)
#novigation keyboard
window.listen()
window.onkeypress(move_up_b,"Up")
window.onkeypress(move_down_b,"Down")
window.onkeypress(move_up,"w")
window.onkeypress(move_down,"s")

#lets create the ball !)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.speed(0)
ball.dx = 3
ball.dy = 3
ball.penup()


# Motion Ball

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = - ball.dy
    if ball.ycor() <= -290:
        ball.dy = - ball.dy

    if ball.xcor() >= 490:
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2,2,3,4])
        ball.dy = choice([-4,-3,-2,2,3,4])
    if ball.xcor() <= -490:
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2,2,3,4])
        ball.dy = choice([-4,-3,-2,2,3,4])

    if ball.ycor() >= rocket_b.ycor() - 50 and ball.ycor() <=rocket_b.ycor()+50 \
        and ball.xcor() >= rocket_b.xcor() -5 and ball.xcor() <= rocket_b.xcor() +5:
        ball.dx = - ball.dx
    if ball.ycor() >= rocket_a.ycor() - 50 and ball.ycor() <=rocket_a.ycor()+50 \
        and ball.xcor() >= rocket_a.xcor() -5 and ball.xcor() <= rocket_a.xcor() +5:
        ball.dx = - ball.dx


window.mainloop()














window.mainloop()
