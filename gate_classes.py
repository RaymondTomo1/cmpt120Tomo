import graphics

from graphics import *


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

class DigitalValue:
    def __init__ (self,p,value):
        self.p = Point(p.getX(),p.getY())
        self.value = int(value)
    
    def getValue(self):
        return self.value
    
    def setValue (self,value):
        self.value = value
    
    def draw(self,win,type):
        if type == 1:
            e = Entry(self.p, 30)
            e.draw(win)
        if type == 2:
            a = str(self.value)
            t = Text(self.p, a )
            t.draw(win)

class And:
    def __init__ (self,p,a,b):
        self.p = Point(p.getX(),p.getY())
        self.a = a
        self.b= b
    
    def setA (self,a):
        self.a = a
    
    def setB (self,b):
        self.b = b
    
    def getOutput (self):
        if self.a.value == 1 and self.b.value == 1:
            return 1
        else:
            return 0
    
    def draw(self,win):
        draw_and (self.p.getX(), self.p.getY(), 20, win)

class Or:
    def __init__ (self,p,a,b):
        self.p = Point(p.getX(), p.getY())
        self.a = a
        self.b= b
    
    def setA (self,a):
        self.a = a
    
    def setB (self,b):
        self.b = b
    
    def getOutput (self):
        if self.a.value == 1 or self.b.value == 1:
         return 1
        else:
         return 0
    
    def draw(self,win):
        draw_or (self.p.getX(), self.p.getY(), 20, win)
    
class Not:
    def __init__ (self,p,a):
        self.p = Point(p.getX(), p.getY())
        self.a = a
    
    
    def setA (self,a):
        self.a = a
    

    def getOutput (self):
        if self.a.value == 1 :
         return 0
        else:
         return 1
    
    def draw(self,win):
        draw_not (self.p.getX(), self.p.getY(), 20, win)

class Xor:
    def __init__ (self,p,a,b):
        self.p = Point(p.getX(), p.getY())
        self.a = a
        self.b= b
    
    def setA (self,a):
        self.a = a
    
    def setB (self,b):
        self.b = b
    
    def getOutput (self):
        if self.a.value == 1 and self.b.value == 1:
            return 0
        if self.a.value == 1 and self.b.value == 0:
            return 1
        if self.a.value == 0 and self.b.value == 1:
            return 1
        if self.a.value == 0 and self.b.value == 0:
            return 0
    
    def draw(self,win):
        draw_xor(self.p.getX(), self.p.getY(), 20, win)
    
class Nand:
    def __init__ (self,p,a,b):
        self.p = Point(p.getX(), p.getY())
        self.a = a
        self.b= b
    
    def setA (self,a):
        self.a = a
    
    def setB (self,b):
        self.b = b
    
    def getOutput (self):
        if self.a.value == 1 or self.b.value == 1:
         return 0
        else:
         return 1
    
    def draw(self,win):
        draw_nand (self.p.getX(), self.p.getY(), 20, win)
    
class Connection:
    def __init__(self, frome, to):
        self.frome = frome
        self.to = to
    
    def getFrom(self):
        return self.frome 
    
    def getTo(self):
        return self.to 


 


def main():
    win1 = GraphWin("Window", 600, 600) 
    aP= Point(50,50)
    bP= Point(80,80)
    cP= Point (100,100)
    dP = Point(500,400)
    eP = Point(200,200)
    a = DigitalValue (aP, 1)
    b = DigitalValue (bP, 1)
    d = DigitalValue (dP, 1)
    Gate1= Nand(cP,a,b)
    Gate2= And(eP,a,b)
    con = Connection(Gate1,Gate2)
    print("A's value is:",a.getValue())
    print("B's value is:",b.getValue())
    print ("Connection from point is:", con.getFrom())
    print ("Connection from point is:", con.getTo())
    print ("Gate1's output value is:",Gate1.getOutput())
    b.setValue(0)
    a.setValue(0)
    print("After changing B, Gate1's output value is:", Gate1.getOutput())
    a.draw(win1,2)
    b.draw(win1,2)
    d.draw(win1,1)
    Gate1.draw(win1)
    



main()

    



    


    



    


