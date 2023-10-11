"""
    Make a program for a paint store. The program should ask for the size in square meters of the area to be painted. Consider that the paint coverage is 1 liter for every 3 square meters and that the paint is sold in 18 liter cans, which costs R$80.00. Inform the user of the pieces of paint cans that will be purchased and the total price.
"""
import math

area = float(input('Type the area in m² to be painted: '))

#Calcutate the total Liters for the input area
def totalLiters(area):
    return int(math.ceil(area / 3))

def totalCan(totalLiters):
    return int(math.ceil(totalLiters / 18))

print('Total area to be painted: {} m²'.format(area))
print('Total liters: {}L'.format(totalLiters(area)))
print('Amount of cans that you need to buy: {}'.format(totalCan(totalLiters(area))))
print('You need to pay R${}'.format(float(totalCan(totalLiters(area)) * 80)))

