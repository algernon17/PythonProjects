import math
import turtle
import tkinter
import random

#def generateRandomParams():
def pat1():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(25)

def main():
    main.colVal = ["blue", "DarkGreen", "DarkViolet", "red", "orange", "green", 
                   "DarkRed", "black", "yellow", "LightBlue", "DarkOrange", "lightgreen", 
                   "magenta", "azure", "coral", "grey", "VioletRed", "LimeGreen", 
                   "firebrick", "GreenYellow", "IndianRed", "LightRed", "MistyRose", "OrangeRed"]
    random.seed()   
    turtle.speed(9)
    turtle.bgcolor("darkgrey")
    realCenterX = 0
    realCenterY = 0
    
    turtle.up()
    turtle.pencolor("DarkRed")
    turtle.setpos(realCenterX, realCenterY)
    turtle.down()

    for i in range(1,13):
        pat1()
        turtle.left(30)
    
    turtle.mainloop()
    
if __name__ == "__main__":
    main()
    