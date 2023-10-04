#Write a program that calculates the area of ​​a square, then shows twice this area to the user.

def calculateSquareArea(length):
    return length * length

squareLength = float(input('Input the lenght of the square: '))

squareArea = calculateSquareArea(squareLength)

print('The area of the square is {} and its double is {}'.format(squareArea, squareArea * 2))