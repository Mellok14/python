import numpy as np
from math import factorial
k, n = 0, 10000
c_ = 0
n_ = 4
k_ = 2
p_ = 0
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k/n)
c_ = factorial(n_)/(factorial(k_)*(factorial((n_ - k_))))
p_ = c_/(2**n_)
print(p_)