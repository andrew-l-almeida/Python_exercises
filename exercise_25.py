"""
Monkey Class: Develop a Monkey class, which has the attributes name and belly (stomach) and at least the methods eat(), seeBelly() and digest(). 
Run a program or test interactively by raising at least two monkeys, feeding them at least 3 different foods, and checking their stomach contents at each meal. Try making one monkey eat another. Is it possible to create a cannibalistic monkey?
"""

class Monkey:
    def __init__(self, name):
        self.name = name
        self.belly = []

    def eat(self, food):
        self.belly.append(food)
    
    def digest(self):
        for food in self.belly:
            if(isinstance(food, Monkey)):
                print('You ate {} and you are a cannibalistic'.format(food.name))
                del food
            else:
                self.belly = []

    def seeBelly(self):
        print(self.belly)

Cezar = Monkey('Cezar')
CapuchinMonkey = Monkey('CapuchinMonkey')

Cezar.eat('Banana')
Cezar.eat('Apple')
Cezar.eat('Lemon')

CapuchinMonkey.eat('Car')
CapuchinMonkey.eat('Van')
CapuchinMonkey.eat('Airplane')

Cezar.seeBelly()
CapuchinMonkey.seeBelly()

Cezar.eat(CapuchinMonkey)

Cezar.seeBelly()
Cezar.digest()
Cezar.seeBelly()


