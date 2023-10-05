#João Papo-de-Pescador, a good man, bought a microcomputer to control his daily work output. Every time he brings a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos) he must pay a fine of R$4.00 per excess kilo. João needs you to write a program that reads the weight variable (fish weight) and calculates the excess. Record in the excess variable the number of kilos beyond the limit and in the fine variable the amount of the fine that João must pay. Print program data with appropriate messages.

def calculateExcessWeight(weight):
    if weight > 50:
        return weight - 50
    else:
        return 0
    
def calculateFine(excessWeight):
    return excessWeight * 4

fishWeight = float(input('Enter the fish weight: '))
excessWeight = calculateExcessWeight(fishWeight)
fine = calculateFine(excessWeight)

if excessWeight == 0:
    print("The fish weighs {}. So the isn't any fine".format(fishWeight))
else:
    print("The fish weighs {} kilos. The excess weight is {}. So you must pay R${}".format(fishWeight, excessWeight,round(fine, 2)))

