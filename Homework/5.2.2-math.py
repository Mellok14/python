import numpy as np
import matplotlib.pyplot as plt
y = 0
for i in range(0,10):
    x = np.random.rand(100)
    y = y + x
num_bins = 10
n, bins, patches = plt.hist(y, num_bins)
plt.xlabel('y')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()