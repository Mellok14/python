import numpy as np
from math import factorial
k, n = 0, 10000
c_ = 0
n_ = 5
k_ = 3
p_ = 0
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 3:
        k = k + 1
print(k, n, k/n)
c_ = factorial(n_)/(factorial(k_)*(factorial((n_ - k_))))
p_ = c_/(2**n_)
print(p_)