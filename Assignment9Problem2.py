#-Design a target to be hit by the cannonbal program

import math

import graphics

import random

from random import*

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

class Target:
    def clicked(self,p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
    def activate(self):
        self.rect.setWidth(2)
        self.active = True
    def deactivate(self):

        self.rect.setWidth(1)
        self.active = False
    def __init__(self,win,center,width,height):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+w, y-w
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("red")
        self.rect.draw(win)
        self.deactivate()

        
        
        
class Projectile:

    def __init__(self,angle,vel,height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = vel*math.cos(theta)
        self.yvel = vel*math.sin(theta)
    def update (self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time *(self.yvel + yvel1) / 2.0
        self.yvel = yvel1
    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos


class InputDialog:

    def __init__(self, angle, vel, height):
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, .5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        Text(Point(1,3), "Height").draw(win)
        self.height = Entry(Point(3,3), 5).draw(win)
        self.height.setText(str(height))
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()
    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
             return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"
            
    def getValues(self):

        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h
    def close(self):
        self.win.close()
class ShotTracker:
    def __init__(self, win, angle, vel, height):
        self.proj = Projectile(angle, vel, height)
        self.marker = Circle(Point(0,height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)
    
    def update(self, dt):
#-update flight pos based on a rate of seconds
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)
    def getX(self):
 #- return the current x 
        return self.proj.getX()
    def getY(self):

        return self.proj.getY()
    def destroy(self):
    #Erase the shot
        self.marker.undraw()



class Tracker:
    def __init__(self, win ,ObjToTrack):
        self.win = win
        self.ObjToTrack = ObjToTrack
        self.xpos = ObjToTrack.getX()
        self.ypos = ObjToTrack.getY()
        self.center = Point(self.xpos, self.ypos)
        self.tracker = Circle(self.center, 5)
    def intiTracker(self):
        self.tracker = Circle(self.center, 5)
        self.tracker.setFill("blue")
        self.tracker.draw(self.win)
    def updateTracker(self,point):
        self.tracker.undraw
        self.center= point
        self.intiTracker()
    def getPosition(self):
        return self.center

def getInputs():
    a =float(input("Enter the launch angle in degrees :"))
    v = float(input("Enter the launch speed in degrees:"))
    h =  float(input("Enter the starting height in meters:"))
    t = float(input("Enter the time interval between calculations in seconds:"))
    return (a,v,h,t)





def main():
    # create animation window
    win = GraphWin("Projectile Animation", 640, 480, autoflush = False)
    win.setCoords(-10, -10, 210, 155)
    # draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    # draw labeled ticks every 50 meters
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)
    # event loop, each time through fires a single shot
    angle, vel, height = 45.0, 40.0, 2.0
    while True:
# interact with the user
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()
        if choice == "Quit":
            break
# create a shot and track until it hits ground or leaves window
        angle, vel, height = inputwin.getValues()
        cball= Projectile(angle,vel,height)
        shot = ShotTracker(win, angle,vel,height)
        shotFollow = Tracker(win, shot)
        targetX = randrange (10, 205)
        targetY= randrange (10, 150)
        targetOne = Target(win, Point(50, 100),10, 10)
        targetOne.activate()
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(50)
            dx = shot.getX()
            dy = shot.getY()
            pt=Point(dx,dy)
            shotFollow.updateTracker(Point(dx,dy))   
            if targetOne.clicked(pt):
                win.close()
                print("You hit the target!") 

main()
