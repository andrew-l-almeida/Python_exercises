# Write and program that that asks 2 integers and a real number. Calculate and show:
"""
    A. The product of twice the first and half the second
    B. The sum of three times the first and third
    C. Third cubed
"""

n1 = int(input('Type a integer: '))
n2 = int(input('Type a second integer: '))
n3 = float(input('Type a float: '))

def calculus1(n1, n2):
    return (2 * n1) * (n2/2)

def calculus2 (n1, n3):
    return ((3*n1) + n3)

def calculus3(n3):
    return n3 **3

print('The result of the first calculus is {}'.format(calculus1(n1, n2)))
print('The result of the second calculus is {}'.format(calculus2(n1, n3)))
print('The result of the third calculus is {}'.format(calculus3(n3)))