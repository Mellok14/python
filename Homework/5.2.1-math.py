#Проверка теоремы сложения на примере выпадения красных или черных ячеек
import numpy as np
k = 0
n = 100000
for i in range(0, n):
    x = np.random.randint(0, 37)
    if x != 0:
        k += 1
    else:
        continue
print(k/n)
#Результат условно равен значению полученному по теореме сложения вероятностей