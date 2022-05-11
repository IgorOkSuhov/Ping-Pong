import turtle
# Creating a playing field

window = turtle.Screen()
window.title('The Game of year Edition: PING-PONG GAME =)')
window.setup(width=1.0,height=1.0)
window.bgcolor('black')

# Denote the boundary of the field

border = turtle.Turtle()
border.color('green')
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
window.mainloop()
