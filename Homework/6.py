a = int(input('Enter first value (km): '))
b = int(input('Enter last value (km): '))
result = False
day = 0
while not result:
    day += 1
    if a >= b:
        result = True
    else:
        a = a*1.1
print (day)
