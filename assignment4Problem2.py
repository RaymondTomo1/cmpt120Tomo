#- These two functions will allow you to get the surface area and volume area of a sphere by inputting a radius

import math



def sphereArea(radius):
    answerArea= 4 * math.pi * (radius * radius)
    return "The surface area of the sphere is:", answerArea
def sphereVolume(radius):
    answerVolume= 4 / 3 * math.pi * (radius * radius *radius)
    return "The volume area of the sphere is:", answerVolume
print(sphereArea(4))
print(sphereVolume(4))