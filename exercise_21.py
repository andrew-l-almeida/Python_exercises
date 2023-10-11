"""
Class Rectangle: Create a class that models a rectangle:

Attributes: SideA, SideB (or Length and Width, or Base and Height, to choose)
Methods: Change side values, Return side values, Calculate Area, and Calculate Perimeter.

Create a program that uses this class.
"""

class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def changeWidth(self, newWidth):
        self.width = newWidth
    
    def changeLenght(self, newLenght):
        self.lenght = newLenght
    
    def getWidht(self):
        return self.width
    
    def calculateArea(self):
        return self.width * self.lenght
    
    def calculatePerimeter(self):
        return (self.width * 2) + (self.lenght * 2)
    

retangle1 = Rectangle(10,20)

print(retangle1.calculateArea())
print(retangle1.calculatePerimeter())

retangle1.changeLenght(50)

print(retangle1.calculateArea())
print(retangle1.calculatePerimeter())

retangle1.changeWidth(45)

print(retangle1.calculateArea())
print(retangle1.calculatePerimeter())