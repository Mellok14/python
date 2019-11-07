from itertools import cycle, count
for el in count(5):
    if el > 55:
        break
    else:
        print(el)

my_list = ['H', 'E', 'L', 'L', 'O', '!']
i = 0
for el in cycle(my_list):
    if i > 20:
        break
    print(el)
    i += 1