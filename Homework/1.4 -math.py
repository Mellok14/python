%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10, 10, 100)
k = 1
plt.plot(x, np.cos(k*x))
k = 3
plt.plot(x, np.cos(k*x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()