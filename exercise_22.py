"""
Person Class: Create a class that models a person:

Attributes: name, age, weight and height
Methods: Getting older, gaining weight, losing weight, growing. Note: By default, every year our person ages, if their age is less than 21 years old, they must grow 0.5 cm.
"""

class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def getOlder(self, age = 1):
        self.age += age
        if(self.age < 21):
            self.height += 0.05
    
    def gainWeight(self, weight):
        self.weight += weight
    
    def lossWeight(self, weight):
        self.weight -= weight

    def grow(self, height):
        self.height += height

andrew = Person('Andrew', 10, 55, 1.3)

andrew.getOlder()

print(andrew.height)

