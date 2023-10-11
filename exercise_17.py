"""
Make a program for a paint store. 
The program should ask for the size in square meters of the area to be painted. Consider that the paint coverage is 1 liter for every 6 square meters, and the paint is sold in 18-liter cans, which cost R$ 80.00, or in 3.6-liter gallons, which cost R$ 25.00. 
Inform the user of the quantities of paint to be purchased and the respective prices in 3 situations: 
buying only 18-liter cans, 
buying only 3.6-liter gallons, 
or mixing cans and gallons to minimize paint waste. 
Add a 10% buffer and always round up the values, meaning consider full cans.
"""
import math

area = float(input('Type the total area in M²: '))

def calculateTotalLiters(area):
    return int(math.ceil(area / 6 * 1.1))

def calculateTotalCan18Liters(liters):
    return int(math.ceil(liters / 18))

def calculatePrice18Liters(liters):
    return calculateTotalCan18Liters(liters) * 80

def calculateTotalCan3_6Liters(liters):
    return int(math.ceil(liters / 3.6))

def calculatePrice3_6Liters(liters):
    return calculateTotalCan3_6Liters(liters) * 25

def mixedCansTotalPrice(liters):
    rest = 0
    price = 0
    if (liters > 18):
        rest = liters % 18
        price = (int(liters / 18) * 80) + (math.ceil(rest / 3.6) * 25)
        return [int(liters / 18), math.ceil(rest / 3.6), price]
    else:
        return False
    
totalLiters = calculateTotalLiters(area)
totalCan18Liters = calculateTotalCan18Liters(totalLiters)
totalCan3_6Liters = calculateTotalCan3_6Liters(totalLiters)
priceCan18Liters = calculatePrice18Liters(totalLiters)
priceCan3_6Liters = calculatePrice3_6Liters(totalLiters)
mixedCans = mixedCansTotalPrice(totalLiters)

def findBest(*options):
    ## 500, 400, 600
    minNumber = 0
    bestOption = 0

    for index, value in enumerate(options):
        if(index == 0):
            minNumber = value
            bestOption = index
        elif(value < minNumber):
            bestOption = index
            minNumber = value
    return str(bestOption + 1)


def printOptions():
    print('')
    print('The area that will be painted is {} m²'.format(area))
    print('')
    print('The total liters that you need is {} L'.format(totalLiters))
    print('')
    print('Option #1: You can buy {} cans of 18L paying: R$ {}'.format(totalCan18Liters, priceCan18Liters))
    print('Option #2: You can buy {} cans of 3.6L paying: R$ {}'.format(totalCan3_6Liters, priceCan3_6Liters))
    if(mixedCans):
        print('Option #3: You can buy {} cans of 18L and {} cans of 3.6L, paying: R$ {}'.format(mixedCans[0], mixedCans[1], mixedCans[2]))
        print('')
        print('The best option for you is the #{}'.format(findBest(priceCan18Liters, priceCan3_6Liters, mixedCans[2])))
    else:
        print('')
        print('The best option for you is the #{}'.format(findBest(priceCan18Liters, priceCan3_6Liters)))
    print('')

printOptions()





