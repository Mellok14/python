import numpy as np
import itertools
for p in itertools.permutations("012356",3):
    print(''.join(str(x) for x in p))
print('---------')
for p in itertools.combinations("012356",3):
    print(''.join(p))