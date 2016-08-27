# ===============================================
# circlePattern2.py
# Peter Swinburne
# May 12th 2016
# ===============================================
import math
import turtle
import random


# ===============================================
# draw circle primative
def drawCircleTurtle(x, y, r, step, colr):
    # move to the start of the circle
    #
    turtle.up()
    turtle.pencolor(colr)
    turtle.setpos(x+r, y)
    turtle.down()

    # draw circle
    for i in range(0, 365, step):
        a = math.radians(i)
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))


# ===============================================
# clear drawing primative
def clearDrawing():
        turtle.clear()


# ===============================================
# set up a drawing and initiate
def setParams():
    colVal = ["blue", "DarkGreen", "DarkViolet", "red",
              "orange", "green", "DarkRed", "black",
              "yellow", "LightBlue", "DarkOrange",
              "lightgreen", "magenta", "azure", "coral",
              "grey", "VioletRed", "LimeGreen",
              "firebrick", "GreenYellow", "IndianRed",
              "LightRed", "MistyRose", "OrangeRed"]
    realCenterX = 0
    realCenterY = 0
    numSides = random.randint(3, 12)

    circStepVal = 360 / numSides
    realCenterStep = 30
    patRad = 50
    radMin = 50
    radMax = 300
    numRings = 20
    radStep = (radMax - radMin) / numRings
    j = 0
    for r in range(radMin, radMax, int(radStep)):
        for i in range(0, 360, realCenterStep):
            a = math.radians(i)
            xc = realCenterX + r * math.cos(a)
            yc = realCenterY + r * math.sin(a)
            drawCircleTurtle(xc, yc, patRad, int(circStepVal), colVal[j])
        j = j + 1
        if(j == len(colVal)):
            j = 0


# ===============================================
# main - start here
def main():
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.onkey(setParams, "s")
    turtle.onkey(clearDrawing, "c")
    turtle.listen()
    turtle.mainloop()


# ===============================================
# the name
if __name__ == "__main__":
    main()


# ===============================================
# Py Module End
# ===============================================
    