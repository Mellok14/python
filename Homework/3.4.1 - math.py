import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 201)
plt.plot(x, x**2 - 1)
plt.plot(x, (np.exp(x) + x - 1)/x)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
from scipy.optimize import fsolve
def equations(p):
    x, y = p
    return (y - x ** 2 + 1, np.exp(x) - x * y + x - 1)
x1, y1 = fsolve(equations, (-2, 1))
print(x1, y1)
x2, y2 = fsolve(equations, (2, 3))
print(x2, y2)
x3, y3 = fsolve(equations, (4, 15))
print(x3, y3)