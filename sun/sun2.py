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
    realCenterX = 10 * (random.randint(0, 20) - 10)
    realCenterY = 10 * (random.randint(0, 20) - 10)
    realRad     = 10 * random.randint(5, 15)
    turtle.up()
    turtle.pencolor(colVal[random.randint(0, 23)])
    turtle.setpos(realCenterX, realCenterY)
    turtle.down()
    numPoints = random.randint(5, 20)
    ang = 180 - (180 / numPoints)
    print(numPoints, ang)
    for n in range(0, numPoints):
        drawRay(realRad)
        turtle.right(ang)
  
# ====================================================
# main function
def main():
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.pensize(3)
    turtle.speed(0)
    for d in range(0, random.randint(4, 10)):
        drawPattern()
    turtle.mainloop()

# ====================================================
# Program Start
if __name__ == "__main__":
    main()
    
