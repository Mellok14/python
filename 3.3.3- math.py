import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0, 2*np.pi, 0.01)
y = 5/np.sin(a-2)
plt.polar(a, y)
plt.show()