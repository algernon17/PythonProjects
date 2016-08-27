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

    #realCenterStep = 360 / random.randint(1, 11)
    #patRad = 10 * random.randint(2, 7)
    #numSides = random.randint(3, 11)
    #circStepVal = 360 / numSides
    #radMin = 10 * random.randint(1, 11)
    #radMax = 30 * random.randint(5, 11)
    #numRings = random.randint(10, 21)
    #radStep = (radMax - radMin) / numRings
    #j = 0
    for n in range(0, 9):
        drawRay(realRad)
        turtle.right(160)

def clearDrawing():#radMin = 10 * random.randint(1, 11)
    turtle.clear()
    
# ====================================================
# main function
def main():
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.pensize(3)
    turtle.speed(0)
    turtle.onkey(drawPattern, "d")
    turtle.onkey(clearDrawing, "c")
    turtle.listen()
    turtle.mainloop()

# ====================================================
# Program Start
if __name__ == "__main__":
    main()
    
