import numpy as np
import matplotlib.pyplot as plt
for k in range(-10,10):
    a = np.linspace(0.01, 0.02, 100)
    plt.plot(a, k*np.pi/a, label=f'k={k}')
axes = plt.gca()
axes.set_ylim([100,500])
plt.legend()
plt.show()