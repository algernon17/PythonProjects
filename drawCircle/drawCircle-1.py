import math
import turtle
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
for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 200 * math.cos(a)
    yc = realCenterY + 200 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "blue")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 175 * math.cos(a)
    yc = realCenterY + 175 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "darkgreen")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 150 * math.cos(a)
    yc = realCenterY + 150 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "red")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 125 * math.cos(a)
    yc = realCenterY + 125 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "orange")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 100 * math.cos(a)
    yc = realCenterY + 100 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "green")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 75 * math.cos(a)
    yc = realCenterY + 75 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "darkred")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 50 * math.cos(a)
    yc = realCenterY + 50 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "black")

for i in range(0, 360, 5):
    a = math.radians(i)
    xc = realCenterX + 25 * math.cos(a)
    yc = realCenterY + 25 * math.sin(a)
    drawCircleTurtle(xc, yc, 50, circStepVal, "yellow")

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

        
