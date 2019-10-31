my_list = [8, 5, 4, 2, 2, 1]
new_list = []
a = input('Введите число: ')
while a != 'Stop':
    for i in my_list:
        if int(a) < i:
            new_list.append(i)
        elif int(a) == i:
            new_list.append(i)
            if i == my_list[-1]:
                new_list.append(int(a))
        elif int(a) > i:
            new_list.append(int(a))
            a = 0
            new_list.append(i)
    print(new_list)
    new_list = []
    a = input('Введите число: ')