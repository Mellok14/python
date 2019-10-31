my_list = []
for i in input('Введите строку, разделяя слова проблемами').split():
    my_list.append(i)
for i, word in enumerate(my_list, 1):
        print(i, word[:10])
