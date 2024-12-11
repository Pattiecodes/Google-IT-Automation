import math

def triangle(base, height):
    return base * height/2

def rectangle(base, height):
    return base * height

def circle(radius):
    return math.pi * (radius ** 2)

#Donut function is used to demonstrate using the Atom Code Editor, 
# integrated in the Atom IDE in a linux machine.
def donut(outside_radius, inside_radius):
    return circle(outside_radius) - circle(inside_radius)