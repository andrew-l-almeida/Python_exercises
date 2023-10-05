"""Create a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary for that month, knowing that 11% are deducted for Income Tax, 8% for INSS and 5% for the union, create a program that gives us:

A. gross salary.
B. how much you paid to INSS.
C .how much he paid to the union.
D . net salary.

Calculate the discounts and net salary, according to the table below:


________INSS Table_________________
Salary (From)   Salary (To)	    Tax
0,00	        1.320,00	    7,5%
1.320,01	    2.571,29	    9,0%
2.571,30	    3.856,94	    12,0%
3.856,95	    7.507,49	    14,0%

____________________________________IR_______________________________________

Base de Cálculo (R$)	            Alíquota (%)	        Dedução do IR (R$)
Até R$ 2.112,00	                    0	                    R$ 0
De R$ 2.112,01 até R$ 2.826,65	    7,5	                    R$ 158,40
De R$ 2.826,66 até R$ 3.751,05	    15	                    R$ 370,40
De R$ 3.751,06 até R$ 4.664,68	    22,5	                R$ 651,73
Acima de R$ 4.664,68	            27,5	                R$ 884,96

"""

def grossSalaryCalculator(amountPerHour, totalHoursWorked):
    return amountPerHour * totalHoursWorked

def inssCalculus(grossSalary):
    if grossSalary <= 1320.00:
        tax = grossSalary * 0.075
    elif grossSalary > 1320.00 and grossSalary <=  2571.29:
        tax = (1320 * 0.075) + ((grossSalary - 1320) * 0.09)
    elif grossSalary > 2571.29 and grossSalary <= 3856.94:
        tax = (1320 * 0.075) + ((2571.29 - 1320) * 0.09) + ((grossSalary - 2571.29) * 0.12)
    elif grossSalary > 3856.94 and grossSalary <= 7507.49:
        tax = (1320 * 0.075) + ((2571.29 - 1320) * 0.09) + ((3856.94 - 2571.29) * 0.12) + ((grossSalary - 3856.94) * 0.14)
    else:
        tax = (1320 * 0.075) + ((2571.29 - 1320) * 0.09) + ((3856.94 - 2571.29) * 0.12) + ((7507.49 - 3856.94) * 0.14)
    return round(tax, 2)

def irCalculator(grossSalary):
    salary = grossSalary - inssCalculus(grossSalary)

    if salary < 2112:
        ir = 0
    elif salary > 2112 and salary <= 2826.65:
        ir = (salary - 2112) * 0.075
    elif salary > 2826.65 and salary <= 3751.05:
        ir = ((2826.65 - 2112) * 0.075) + (salary - 2826.65) * 0.15
    elif salary > 3751.05 and salary <= 4664.68:
        ir = ((2826.65 - 2112) * 0.075) + ((3751.05 - 2826.65) * 0.15) + ((salary - 3751.05) * 0.225)
    else:
        ir = ((2826.65 - 2112) * 0.075) + ((3751.05 - 2826.65) * 0.15) + ((4664.68 - 3751.05) * 0.225) + ((salary - 4664.68) * 0.275)
    return ir

def syndicateCalculus(grossSalary):
    salary = grossSalary - inssCalculus(grossSalary) - irCalculator(grossSalary)
    return salary * 0.05

def netSalaryCalculus(grossSalary):
    return (grossSalary - inssCalculus(grossSalary) - irCalculator(grossSalary) - syndicateCalculus(grossSalary))

hoursWorked = int(input('Type the amount of hours: '))
salaryPerHour = float(input('Type the amount you receive per hour: R$'))
grossSalary = grossSalaryCalculator(salaryPerHour, hoursWorked)
totalInss = inssCalculus(grossSalary)
totalIR = irCalculator(grossSalary)
totalSyndicate = syndicateCalculus(grossSalary)
netSalary = netSalaryCalculus(grossSalary)

text = 'Total Amount'
print('_' * 32)
print('_' * int(((30 - len(text))/2)), text ,'_' * int(((30 - len(text))/2)) )
print('_' * 32)
print('Gross salary: R$ {}'.format(round(grossSalary,2)))
print('Total INSS: R$ {}'.format(inssCalculus(round(grossSalary,2))))
print('Total IR: R$ {}'.format(round(totalIR,2)))
print('Total syndicate: R$ {}'.format(round(totalSyndicate,2)))
print('Net salary: R$ {}'.format(round(netSalary,2)))
print('_' * 32)
print('_' * 32)