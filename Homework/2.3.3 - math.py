import matplotlib.pyplot as plt
import math
x = []
y = []
y1 = []
y2 = []
y3= []
for i in range(200, 500):
    x_ = i/100
    x.append(x_)
    y.append(math.sqrt(-9*(1-x_**2/4)))
    y1.append(-math.sqrt(-9 * (1 - x_ ** 2 / 4)))
for i in range(-500, -199):
    x_ = i / 100
    x.append(x_)
    y.append(math.sqrt(-9 * (1 - x_ ** 2 / 4)))
    y1.append(-math.sqrt(-9 * (1 - x_ ** 2 / 4)))
plt.plot(x,y)
plt.plot(x,y1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()