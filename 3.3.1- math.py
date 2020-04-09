import numpy as np
def poltodecart(r, a):
    x = r*np.cos(a)
    y = r*np.sin(a)
    return x, y
print(poltodecart(3, 2))