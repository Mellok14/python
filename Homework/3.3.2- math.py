import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, np.pi, 180)
y = 3*np.sin(x)
plt.polar(x, y)
plt.show()