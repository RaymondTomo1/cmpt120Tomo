#-This program allows the user to draw a line segment with the click of their mouse and displays info about the line segment

import math

from graphics import *

def main():
    win= GraphWin()
    click1= win.getMouse()
    click1X =click1.getX()
    click1Y =click1.getY()
    click2= win.getMouse()
    click2X =click2.getX()
    click2Y =click2.getY()
    aLine=Line(Point(click1X,click1Y),Point(click2X,click2Y))
    aLine.draw(win)
    midpoint = aLine.getCenter()
    midpointX= midpoint.getX()
    midpointY= midpoint.getY()
    midpoint1 = Point(midpointX,midpointY)
    midpoint1.setFill("cyan")
    midpoint1.draw(win)
    dx= click2X-click1X
    dy=click2Y-click1Y
    slope= (dy/dx)
    lengthOfLine= math.sqrt((dy*dy)+(dx* dx))
    print ("The slope of the line is:", slope)
    print ("The length of the line is", lengthOfLine)
main()
