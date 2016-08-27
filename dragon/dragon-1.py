#=================================================
# dragon-1.py
#=================================================
import math
import turtle
import time
import random

# ====================================================
# draw a circle using turtle 
def drawSegment(ang, seglen):
    # move to the start of the circle
    turtle.up()
    turtle.setpos(drawDragon.x, drawDragon.y)
    turtle.down()
    drawDragon.a = drawDragon.a + ang
    turtle.setheading(drawDragon.a)
    h = seglen / 3
    
    # draw segment
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(h)
    tup1 = turtle.position()
    drawDragon.x = tup1[0]
    drawDragon.y = tup1[1]

# ====================================================
def clearDrawing():
    turtle.clear()

# ====================================================
def drawDragon():
    drawDragon.x = -250
    drawDragon.y = 0
    drawDragon.a = 0
    drawSegment(45, 250)
    drawSegment(90, 250)
    drawSegment(90, 250)
    drawSegment(90, 250)
    
# ====================================================
# main function
def main():
    main.indx = 1
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.mode("logo")
    turtle.onkey(drawDragon, "s")
    turtle.onkey(clearDrawing, "c")
    turtle.listen()

    # move to the start of the dragon
    turtle.up()
    turtle.pencolor("DarkBlue")
    turtle.setpos(0, 0)
    turtle.down()

    turtle.mainloop()

# ====================================================
# Program Start
if __name__ == "__main__":
    main()
    
