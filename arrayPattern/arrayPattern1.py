import math
import turtle
import random
import time

patArray = [0,0,0,0,0,
            1,1,1,1,1,
            2,2,2,2,2,
            3,3,3,3,3,
            4,4,4,4,4]
colArray = ["blue", "blue", "blue", "blue", "blue",
            "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen",
            "DarkViolet", "DarkViolet", "DarkViolet", "DarkViolet", "DarkViolet", 
            "IndianRed", "IndianRed", "IndianRed", "IndianRed", "IndianRed", 
            "DarkOrange", "DarkOrange", "DarkOrange", "DarkOrange", "DarkOrange"]

# ====================================================
# main function
def randomizePatArr():
    for l in range(0, 400):
        j = random.randint(0,24)
        k = random.randint(0,24)
        l = patArray[j]
        patArray[j] = patArray[k]
        patArray[k] = l
        j = random.randint(0,24)
        k = random.randint(0,24)
        l = colArray[j]
        colArray[j] = colArray[k]
        colArray[k] = l
        
def pat1(x, y, segLen):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setpos(x+segLen, y+segLen)
    turtle.setpos(x, y+segLen)
    turtle.setpos(x+segLen, y)
    turtle.setpos(x, y)
    turtle.penup()

def pat2(x, y, segLen):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setpos(x, y+segLen)
    turtle.setpos(x+segLen, y)
    turtle.setpos(x+segLen, y+segLen)
    turtle.setpos(x, y)
    turtle.penup()

def pat3(x, y, segLen):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setpos(x+segLen, y+segLen)
    turtle.penup()
    turtle.setpos(x+segLen, y)
    turtle.pendown()
    turtle.setpos(x, y+segLen)
    turtle.penup()

def pat4(x, y, segLen):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.circle(segLen/2,180)
    turtle.penup()
    turtle.setpos(x+segLen, y+segLen)
    turtle.pendown()
    turtle.circle(segLen/2,180)
    turtle.penup()

def pat5(x, y, segLen):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(segLen/2,-180)
    turtle.penup()
    turtle.setpos(x+segLen, y+segLen)
    turtle.pendown()
    turtle.circle(segLen/2,-180)
    turtle.left(90)
    turtle.penup()

def main():
    random.seed()
    turtle.bgcolor("darkgrey")
    turtle.speed(0)
    currXs = -250
    currYs = -250
    currX = currXs
    currY = currYs
    turtle.pensize(3)
    turtle.clear()
    randomizePatArr()
    patlen  = 20
    for l in range(0, 21):
        for m in range(0, 21):
            currX = currXs + (l * patlen)
            currY = currYs + (m * patlen)
            c = (l + m) % 25
            turtle.color(colArray[c])
            if(patArray[l] == 0):
                pat1(currX, currY, patlen)
            if(patArray[l] == 1):
                pat2(currX, currY, patlen)
            if(patArray[l] == 2):
                pat3(currX, currY, patlen)
            if(patArray[l] == 3):
                pat4(currX, currY, patlen)
            if(patArray[l] == 4):
                pat5(currX, currY, patlen)
    turtle.mainloop()

# ====================================================
# Program Start
if __name__ == "__main__":
    main()
    
