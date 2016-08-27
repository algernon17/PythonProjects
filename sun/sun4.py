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
    realCenterX = 0
    realCenterY = 0
    realRadius = 200
    numPoints = 9
    numSuns = 15
    colIndx = 4
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
        drawRay(sunRad / 2)
        turtle.right(ang)
  
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
    
