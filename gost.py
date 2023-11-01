import turtle, time

donatello = turtle.Turtle()

donatello.right(90)
donatello.forward(200)


for i in range(5):
    donatello.right(45)
    donatello.forward(25)
    donatello.right(90)
    donatello.forward(25)
    donatello.left(135)

donatello.right(180)
donatello.forward(200)
# donatello.right(180)
donatello.circle(-88, 180)

# eye 1
donatello.color("white")
donatello.right(90)
donatello.forward(50)
donatello.color("Black")
donatello.fillcolor("Black")
donatello.begin_fill()
donatello.circle(15)
donatello.end_fill()

# eye 2
donatello.color("white")
donatello.forward(70)
donatello.color("Black")
donatello.fillcolor("Black")
donatello.begin_fill()
donatello.circle(15)
donatello.end_fill()
donatello.circle(15, 180)


# mouth 
donatello.right(90)
donatello.color("white")
donatello.forward(70)
donatello.color("Black")
donatello.fillcolor("Black")
donatello.begin_fill()
donatello.left(90)
donatello.forward(70)
donatello.right(90)
donatello.circle(-35, 180)
donatello.end_fill()



donatello.screen.mainloop()