import math
import turtle
from datetime import datetime
import time
import random

# ====================================================
# draw a circle using turtle 
def drawCircleTurtle(x, y, r, step, colr):
    # move to the start of the circle
    turtle.up()
    turtle.pencolor(colr)
    turtle.setpos(x+r, y)
    turtle.down()

    # draw circle
    for i in range(0, 365, step):
        a = math.radians(i)
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))

# ====================================================
# Program Start
random.seed()
turtle.bgcolor("darkgrey")
colVal = ["blue", "darkgreen", "DarkViolet", 
          "red", "orange", "green", 
          "darkred", "black", "yellow", 
          "lightblue", "lightgreen", "grey",
          "LimeGreen", "magenta", "azure",
          "coral", "DarkOrange", "VioletRed",
          "firebrick", "GreenYellow", "IndianRed",
          "LightBlue", "MistyRose", "OrangeRed"]
realCenterX = 0
realCenterY = 0
realCenterStep = 360 / random.randint(1, 11)
patRad = 10 * random.randint(2, 7)
numSides = random.randint(3, 11)
turtle.clear()
circStepVal = 360 / numSides
radMin = 10 * random.randint(1, 11)
radMax = 30 * random.randint(5, 11)
numRings = random.randint(10, 21)
radStep = (radMax - radMin) / numRings
j = 0
for r in range(radMin, radMax, int(radStep)):
    turtle.pensize(random.randint(1, 4))
    for i in range(0, 360, int(realCenterStep)):
        a = math.radians(i)
        xc = realCenterX + r * math.cos(a)
        yc = realCenterY + r * math.sin(a)
        drawCircleTurtle(xc, yc, patRad, int(circStepVal), colVal[j])
    j = j + 1
    if(j == len(colVal)):
        j = 0
#time.sleep(30)
    
turtle.mainloop()
