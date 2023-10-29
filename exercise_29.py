#Calculo do primeiro digito do CPF

cpf = '477928708'

cpfSum = 0
for i, n in enumerate(cpf):
    cpfSum += int(n) * (10 - i)

dig1 = (cpfSum * 10) % 11

dig1 = 0 if dig1 > 9 else dig1

cpf2 = cpf + str(dig1)

cpfSum2 = 0
for i, n in enumerate(cpf2):
    cpfSum2 += int(n) * (11 - i)

dig2 = (cpfSum2 * 10) % 11

print(dig1, dig2)
