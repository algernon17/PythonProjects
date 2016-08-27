import math
import turtle
import time
import random

# ====================================================
# draw a circle using turtle 
def drawRay(r):
    # move to the start of the circle
    turtle.circle(r, 60)
    turtle.circle(-r, 60)
    
# ====================================================
# drawPattern function
def drawPattern():
    colVal = ["blue", "DarkGreen", "DarkViolet", 
              "red", "orange", "green", 
              "darkred", "black", "yellow", 
              "firebrick", "LightGreen", "grey",
              "LimeGreen", "magenta", "azure",
              "coral", "DarkOrange", "VioletRed",
              "cyan", "GreenYellow", "IndianRed",
              "LightBlue", "MistyRose", "OrangeRed"]
    realCenterX = -320
    realCenterY = 50
    realRadius = 75
    numPoints = 5
    numSuns = 15
    colIndx = 0
    for d in range(0, numSuns):
        sunRad = 75
        turtle.up()
        turtle.pencolor(colVal[colIndx])
        turtle.setpos(realCenterX, realCenterY)
        turtle.circle(realRadius, 360 / numSuns)
        turtle.down()
        ang = 180 - (180 / numPoints)

        for n in range(0, numPoints):
            drawRay(sunRad)
            turtle.right(ang)
        realCenterX = realCenterX + 40
        #realCenterY = realCenterY - 40
        numPoints = numPoints + 2
        colIndx = colIndx + 1
  
# ====================================================
# main function
def main():
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.pensize(3)
    turtle.speed(0)
    drawPattern()
    turtle.mainloop()

# ====================================================
# Program Start
if __name__ == "__main__":
    main()
    
