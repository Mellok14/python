import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-30, 30, 10)
Y = np.arange(-30, 30, 10)
print(X)
X, Y = np.meshgrid(X, Y)
Z = 2*X + 3*Y + 55
Z2 = 2*X + 3*Y
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z2)
show()