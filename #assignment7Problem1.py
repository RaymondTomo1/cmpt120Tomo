#This program will simulate an archery target using the graphics library

import graphics 

from graphics import *

def main():
    win = graphics.GraphWin()
    c1 = Circle(Point(50,50), 10)
    c1.setFill("white")
    c1.draw(win)
    c2 = Circle(Point(50,50), 8)
    c2.setFill("black")
    c2.draw(win)
    c3=Circle(Point(50,50), 6)
    c3.setFill("blue")
    c3.draw(win)
    c4=Circle(Point(50,50), 4)
    c4.setFill("red")
    c4.draw(win)
    c5=Circle(Point(50,50), 2)
    c5.setFill("yellow")
    c5.draw(win)

main()
