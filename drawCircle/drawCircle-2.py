import math
import turtle
£from datetime import datetime
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

circStepVal = 24
realCenterX = 0
realCenterY = 0
for r in range(25, 200, 25):
    for i in range(0, 360, 5):
        a = math.radians(i)
        xc = realCenterX + r * math.cos(a)
        yc = realCenterY + r * math.sin(a)
        drawCircleTurtle(xc, yc, 50, circStepVal, "blue")

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

        
