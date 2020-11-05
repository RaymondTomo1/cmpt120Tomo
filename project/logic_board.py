#This will create a logic board with buttons that allow you to draw buttons

import graphics

from graphics import*




class Button:
    def clicked(self,p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True
    def deactivate(self):
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    def __init__(self,win,center,width,height,label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+w, y-w
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label= Text(center, label)
        self.label.draw(win)
        self.deactivate()

    
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

def draw_not(x,y,size,win):
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
    

def draw_xor(x,y,size,win):
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


def draw_nand(x,y,size,win):
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



centerPoint= Point(30,30)





def main():
    #-Draw Board
    logicBoard =  GraphWin("Logic Board", 600, 600)
    #-Draw Buttons
    andButton = Button(logicBoard, Point(30, 30), 50, 50, "AND" )
    orButton = Button(logicBoard, Point(30, 90), 50, 50, "OR" )
    notButton= Button(logicBoard, Point(30, 150), 50, 50, "NOT" )
    xorButton= Button(logicBoard, Point(30, 210), 50, 50, "XOR" )
    nandButton= Button(logicBoard, Point(30, 270), 50, 50, "NAND" )
    #-Draw Events
    andButton.activate()
    orButton.activate()
    notButton.activate()
    xorButton.activate()
    nandButton.activate()
    clickpoint = logicBoard.getMouse()
    clickX= int(clickpoint.getX())
    clickY= int(clickpoint.getY())
    pt = logicBoard.getMouse()
    if andButton.clicked(pt):
        draw_and(clickX,clickY,50,logicBoard)
    elif orButton.clicked(pt):
        draw_or(clickX,clickY,50,logicBoard)
    elif notButton.clicked(pt):
        draw_not(clickX,clickY,50,logicBoard)
    elif xorButton.clicked(pt):
        draw_xor(clickX,clickY,50,logicBoard)
    elif nandButton.clicked(pt):
        draw_nand(clickX,clickY,50,logicBoard)
    

main()
    
        







