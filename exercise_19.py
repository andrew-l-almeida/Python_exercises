"""
    Class Ball: Create a class that models a ball:

    Attributes: Color, circumference, material
    Methods: changeColor and showColor
"""

class Circle:
    def __init__(self, color, circumference, material):
        self.color = color
        self.circumference = circumference
        self.material = material
    
    def changeColor(self, color):
        self.color = color

    def showColor(self):
        print(self.color)

circle1 = Circle('red', 10, 'I-304')

circle1.changeColor('Blue')
circle1.showColor()