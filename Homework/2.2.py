my_list = []
for i in input('Введите элемент списка через пробел').split():
    my_list.append(i)
print('Первоначальный список:')
print(my_list)
for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print('Конечный список:')
print (my_list)