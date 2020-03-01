import numpy as np
for i in range(0, 10):
    a = input('Move roulette!')
    x = np.random.randint(0, 37)
    if x == 0:
        print("Zero")
    else:
        print(x)