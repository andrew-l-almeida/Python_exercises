#Make a program that asks how much do you earn per hour and the total hours worked in the month. Calculate the total salary

def totalSalary(hours, amountPerHour):
    return hours * amountPerHour

workedHours = float(input('How much hours did you work this month?: '))
salaryPerHour = float(input('How much do you earn per hour?: '))

print('Your total amount that you will earn is ${}'.format(round(totalSalary(workedHours, salaryPerHour),2)))