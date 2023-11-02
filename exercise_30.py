def multiplicator(*args):
    total = 1
    for n in args:
        total *= n
    return total

m = multiplicator(1,2,3,4,5,6,7,8,9)
print(m)