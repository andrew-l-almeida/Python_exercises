"""
Class Tamagochi: Create a class that simulates a tamagushi

Attributes: Name, Hunger, Health and age

Methods: Change name, hunger, health and age. Return name, hunger, health and age. The humor of our tamagushi is the combination of the attributes hunger and health, a calculated field, so we don't have to create a attribute to store this information because it can be calculated any time
"""
class Tamagotchi:
    def __init__(self, name, hunger, health, age):
        self.name = name
        self.__alive = True

        if(hunger <= 0 or hunger > 100):
            print('Hunger has to be between 1 and 100')
            newHunger = hunger
            while (newHunger <=0 or newHunger >100):
                newHunger = int(input('Type the new hunger: '))
            self.hunger = newHunger
        else:
            self.hunger = hunger

        if(health <=0 or health > 100):
            newHealth = health
            print('Health has to be between 1 and 100')
            while(newHealth <=0 or newHealth > 100):
                newHealth = int(input('Type the new health: '))
            self.health = newHealth
        else:
            self.health = health

        if(age <=0 or age > 100):
            newAge = age
            print('Age has to be between 1 and 100')
            while(newAge <=0 or newAge > 100):
                newAge = int(input('Type new Age: '))
            self.age = newAge
        else:
            self.age = age
    
    def isAlive(self):
        return self.__alive
    def passAway(self, reason):
        self.__alive = False
        print('You passed away because of {}'.format(reason))


    def getName(self):
        if(self.__alive):
            return self.name
        else:
            print("I'm sorry, but {} is dead".format(self.name))
    def setName(self, newName):
        if(self.__alive):
            self.name = newName
        else:
            print("I'm sorry, but {} is dead".format(self.name))
    
    def getHunger(self):
        if(self.__alive):
            return self.hunger
        else:
            print("I'm sorry, but {} is dead".format(self.name))
    
    def setHunger(self, newHunger):
        if(newHunger <=0 or newHunger >100):
            self.hunger = newHunger
            self.passAway('Hunger')
        else:
            self.hunger = newHunger

    def eat(self, amount):
        if(self.__alive):
            if(self.hunger + amount > 100):
                print('You are not that hungry!!!')
            else:
                self.hunger += amount
        else:
            print("I'm sorry, but {} is dead".format(self.name))
        
    def getHealth(self):
        if(self.__alive):
            return self.health
        else:
            print("I'm sorry, but {} is dead".format(self.name))
    
    def setHealth(self, newHealth):
        if(newHealth <=0):
            self.passAway('Health')
        elif(newHealth > 100):
            print('Your health has to be between 1 and 100')
        else:
            self.health = newHealth

    def getAge(self):
        if(self.__alive):
            return self.age
        else:
            print("I'm sorry, but {} is dead".format(self.name))

    def setAge(self, newAge):
        if(newAge <=0):
            print("You can't type a age <= 0")
        elif(newAge < self.age):
            print("You can't go back in time!")
        elif(newAge > 100):
            self.passAway('Age')
        else:
            self.age = newAge
        
    def getHumor(self):
        #65 Hunger - 35 - Health
        if(self.__alive):
            return ((self.hunger * 65) + (self.health * 35)) / 100
        else:
            print("I'm sorry, but {} is dead".format(self.name))

andrew = Tamagotchi('Andrew', 50, 50, 22)

andrew.eat(20)
print(andrew.getHunger())

andrew.setHunger(0)

print(andrew.getAge())
