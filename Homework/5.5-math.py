import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n
r_ = np.sum((x-np.sum(x)/n)*(y-np.sum(y)/n))/sqrt(np.sum((x-np.sum(x)/n)**2)*np.sum((y-np.sum(y)/n)**2))
c = np.corrcoef(x, y)
A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
print(c)
print(r_)
plt.plot([0, 1], [b, a + b])
plt.show()