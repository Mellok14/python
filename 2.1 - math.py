from math import sqrt
vect = [3, 4]
summ = 0
for i in range(len(vect)):
    summ += vect[i]**2
len_vect = sqrt(summ)
print(len_vect)