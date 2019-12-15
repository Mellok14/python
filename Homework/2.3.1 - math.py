import matplotlib.pyplot as plt
import math
x = []
y = []
y1 = []
for i in range(-500, 501):
    x_1 = i/100
    x.append(x_1)
    y.append(math.sqrt(25 - x_1**2))
    y1.append(-math.sqrt(25 - x_1** 2))
plt.plot(x,y)
plt.plot(x,y1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()