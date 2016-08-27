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
    realCenterX = -100
    realCenterY = 0
    realRadius = 200
    numPoints = 11
    numSuns = 15
    colIndx = 4
    sunRad = 75
    turtle.up()
    turtle.setpos(realCenterX, realCenterY)
    turtle.circle(realRadius, 360 / numSuns)
    turtle.down()
    ang = 180 - (180 / numPoints)
    for n in range(0, numPoints):
        turtle.pencolor(colVal[4])
        drawRay(sunRad)
        turtle.right(ang)
        drawRay(sunRad)
        turtle.right(ang)
        turtle.pencolor(colVal[3])
        drawRay(sunRad / 2)
        turtle.right(ang)
        drawRay(sunRad / 2)
        turtle.right(ang * 2)
  
# ====================================================
# main function
def main():
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.pensize(2)
    turtle.speed(0)
    drawPattern()
    turtle.mainloop()

# ====================================================
# Program Start
if __name__ == "__main__":
    main()
    
