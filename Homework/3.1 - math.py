import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4*np.pi, 4*np.pi, 201)
plt.plot(x, 3*np.cos(x - np.pi/4) + 5)
plt.plot(x, 2*np.cos(x - np.pi/6) + 3)
plt.plot(x, 4*np.cos(x - np.pi/2) + 2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
