import math
import turtle
from datetime import datetime

colVal = ["blue", "darkgreen", "darkgrey", "red", "orange", "green", "darkred", "black", "yellow", "lightblue", "lightgreen", "grey"]

# draw a circle using turtle 
def drawCircleTurtle(x, y, r, step, colr):
    # move to the start of the circle
    turtle.up()
    turtle.pencolor(colr)
    turtle.setpos(x, y)
    turtle.down()

    # draw circle
    turtle.circle(r)    

def main():
    turtle.clear()
    turtle.speed(0)
    circStepVal = 9
    realCenterX = 0
    realCenterY = 0
    realCenterStep = 18
    patRad = 50
    radMin = 22
    radMax = 250
    radStep = (radMax - radMin) / 50
    j = 0
    for r in range(radMin, radMax, int(radStep)):
        for i in range(0, 360, realCenterStep):
            a = math.radians(i)
            xc = realCenterX + r * math.cos(a)
            yc = realCenterY + r * math.sin(a)
            drawCircleTurtle(xc, yc, patRad, circStepVal, colVal[j])
        j = j + 1
    
    turtle.hideturtle()
    #generate a unique filename
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'spiro-' + dateStr
    # get the tkinter canvas
    canvas = turtle.getcanvas()
    # save drawing as a postscript image
    canvas.postscript(file = fileName + '.eps')
    # use the Pillow module to convert the postscript file to PNG
    #img = Image.open(fileName + '.eps')
    #img.save(fileName + '.png', 'png')
    turtle.showturtle()
    turtle.mainloop()

if __name__ == "__main__":
    main()
