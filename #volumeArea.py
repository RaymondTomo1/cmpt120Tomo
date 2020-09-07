#volumeAndArea
#This program will allow you to find the volume and circumfrence of different objects

import math
def volumeOperation():
        print ("This program will allow you to calculate the volume of a sphere")
        radius = eval(input("Input the radius here"))
        volume = 4 / 3 * math.pi * (radius * radius *radius)
        area = 4 * math.pi * (radius * radius)
        print("The volume of the sphere is:", volume)
        print("The area of the sphere is:", area)
volumeOperation()
    
