# Write a Program that asks for the radius of a circle, calculates and displays its area.
import math
radius = float(input('Type the circle radius to calculate its area: '))

def circleArea(radius):
    return 3.14159265 * radius * radius

print('The area of a circle with radius {} is: {}'.format(radius, math.ceil(circleArea(radius))))   