import math
import turtle
import tkinter
import random

#==========================================================
def patSeg(segLen, lrDir):
    turtle.forward(segLen)
    if lrDir == 0:
        turtle.left(90)
    else:
        turtle.right(90)       

#==========================================================
def pat1():
    patSeg(100, 0)
    patSeg(25, 0)
    patSeg(25, 0)
    patSeg(100, 0)
    patSeg(50, 0)
    patSeg(125, 0)
    patSeg(75, 0)
    patSeg(75, 0)
    patSeg(25, 1)
    
   
#==========================================================
def main():
    main.colVal = ["blue", "coral", "DarkViolet", "red", "orange", "green", 
                   "DarkRed", "black", "yellow", "LightBlue", "DarkOrange", "lightgreen", 
                   "magenta", "azure", "coral", "grey", "VioletRed", "LimeGreen", 
                   "firebrick", "GreenYellow", "IndianRed", "MistyRose", "OrangeRed"]
    random.seed()   
    turtle.speed(9)
    turtle.bgcolor("darkgrey")
    realCenterX = 0
    realCenterY = 150

    turtle.up()
    turtle.setpos(realCenterX, realCenterY)
    turtle.down()
    turtle.pensize(2)
    colindx = 0
    main.stop = 0
    while main.stop == 0:
        for deltaAng in range(60,15,-15):
            turtle.pencolor(main.colVal[colindx])
            colindx = colindx + 1
            if colindx == 23:
                colindx = 0
            curX = 1
            curY = 1
            while (curX != 0) and (curY != 0):
                pat1()
                turtle.left(deltaAng)
                pos = turtle.position()
                curX = int(pos[0] - realCenterX)
                curY = int(pos[1] - realCenterY)
                #print(pos)
        
            turtle.pencolor("darkgrey")
            curX = 1
            curY = 1
            while (curX != 0) and (curY != 0):
                pat1()
                turtle.left(deltaAng)
                pos = turtle.position()
                curX = int(pos[0] - realCenterX)
                curY = int(pos[1] - realCenterY)
                #print(pos)
    
    #turtle.mainloop()
    # 60 : 12
    # 45 : 8
    # 30 : 6
    
#==========================================================
if __name__ == "__main__":
    main()
    