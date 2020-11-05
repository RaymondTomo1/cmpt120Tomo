#This program will define and draw multiple logic gates 

import graphics

from graphics import *

win = GraphWin()



def main ():
    # This will draw a gate for the user
    draw_xor(20,20,30,win)



def draw_and(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

# Function to draw an OR gate
def draw_or(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_not(x,y,size,window):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    #Outline
    Polygon(Point(x1,y1), Point(x+size,y), Point (x1,y2)).draw(win)
    Circle(Point(x2+x/1.5,y),size/15).draw(win)
    #Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x2+x/1.5,y),Point(x2+size+10,y)).draw(win)
    
    

def draw_xor(x,y,size,window):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    #Outline
    Arc(Point(x1-size/2-10,y1),Point(x1+size/2-10,y2)).draw(win)
    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)


def draw_nand(x,y,size,window):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    Circle(Point(x2+x,y),size/15).draw(win)
    # Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)
main()
