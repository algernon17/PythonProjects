import math
import turtle

# draw a circle using turtle
def drawCircleTurtle(x, y, r):
    # move to the start of the circle
    turtle.penup()
    turtle.setpos(x + r, y)
    turtle.pendown()

    # draw the circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))

drawCircleTurtle(100, 100, 50)
turtle.mainloop()
