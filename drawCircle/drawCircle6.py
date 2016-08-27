import math
import turtle
from datetime import datetime
import time
#from PIL import Image

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

#def generateRandomParams():
#    rcs = random.randint

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

for numSides in range (3, 12, 1):
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
    time.sleep(20)
    turtle.clear()
    
#turtle.hideturtle()
#generate a unique filename
#dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
#fileName = 'spiro-' + dateStr
# get the tkinter canvas
#canvas = turtle.getcanvas()
# save drawing as a postscript image
#canvas.postscript(file = fileName + '.eps')
# use the Pillow module to convert the postscript file to PNG
#img = Image.open(fileName + '.eps')
#img.save(fileName + '.png', 'png')
#turtle.showturtle()
turtle.mainloop()
