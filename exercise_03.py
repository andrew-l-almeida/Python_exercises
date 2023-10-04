# Create a program that asks for the 4 bimonthly grades and shows the average.

grades = []

amount = int(input('How many grades?: '))

for x in range(1,amount+1):
    grades.append(float(input('Note number {}: '.format(x))))

def gradeAverage(grades):
    x = 0
    for grade in grades:
        x += grade
    return x / len(grades)

print(gradeAverage(grades))