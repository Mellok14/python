import numpy as np
import scipy
import scipy.linalg
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def Q(x, y, z):
    return (x**2 + y**2 + z**2)
fig = figure()
ax = Axes3D(fig)
x = np.linspace(-5, 5, 201)
y = np.linspace(-5, 5, 201)
ax.plot(x, y, Q(x, y, (-7*x + 7*y +11)/3))
plt.show()
A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
print(np.linalg.lstsq(A, B))
