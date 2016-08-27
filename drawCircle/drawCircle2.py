import math
import turtle

# draw a circle using turtle
def drawCircleTurtle(x, y, r, step):
	# move to the start of the circle
	turtle.up()
	turtle.setpos(x + r, y)
	turtle.down()
	
	# draw the circle
	for i in range(0, 365, step):
	 a = math.radians(i)
	 turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))
	 
for i in range(0, 365, 15):
	a = math.radians(i)
	xc = 100 + 200 * math.cos(a)
	yc = 100 + 200 * math.sin(a)
	drawCircleTurtle(xc, yc, 50, 120)
	
turtle.mainloop()
