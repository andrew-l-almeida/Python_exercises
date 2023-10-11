"""
Class Square: Create a class that models a square:

Attributes: Side Length
Methods: Change Side Length, Return Side Length, and Calculate Area.
"""

class Square:
    def __init__(self, sideLength):
        self.sideLenght = sideLength

    def changeSideLenght(self, sideLenght):
        self.sideLenght = sideLenght
    
    def length(self):
        return self.sideLenght
    
    def calculateArea(self):
        return self.sideLenght * self.sideLenght

square1 = Square(50)

square1.changeSideLenght(80)

print(square1.length())
print(square1.calculateArea())