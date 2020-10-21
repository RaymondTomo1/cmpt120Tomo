#- This program will draw a line through a given circle based on the radius and other information given



radius1 = eval(input("Enter the radius of the circle here:"))
yInt= eval (input("Enter the y-intercept here:"))

import math

import graphics

from graphics import *

def main():
    win= graphics.GraphWin()
    win.setCoords(-10,-10,10,10)
    circ=Circle(Point(0, 0), radius1)
    circ.draw(win)
    aLine= Line(Point(-10,yInt), Point(10 ,yInt))
    aLine.draw(win)
    x1= math.sqrt((radius1*radius1)-(yInt*yInt))
    x2= -math.sqrt((radius1*radius1)-(yInt*yInt))
    point1= Point(x1, yInt)
    point1.setFill("red")
    point1.draw(win)
    point2= Point(x2,yInt)
    point2.setFill("red")
    point2.draw(win)
    print ("The first x value is", x1)
    print ("The second x value is", x2)



main()






