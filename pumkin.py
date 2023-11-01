

import turtle

turtle.bgcolor("white")
turtle.pensize(2)
turtle.speed(2)

# Draw the stem
turtle.color("dark green")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10, 360)
turtle.end_fill()

# Draw the pumpkin
turtle.color("orange")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Draw the eyes
turtle.color("black")
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(30, 50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# Draw the mouth
turtle.color("black")
turtle.penup()
turtle.goto(-50, -30)
turtle.pendown()
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(30)

turtle.done()