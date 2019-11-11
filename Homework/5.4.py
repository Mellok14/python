with open('text_5.4.1.txt', 'r') as file_1:
    with open('text_5.4.2.txt', 'w', encoding='utf-8') as file_2:
        number_list = ['Один', 'Два', 'Три', 'Четыре']
        i = 0
        for line in file_1:
            my_list = line.split()
            file_2.write(f'{number_list[i]} — {my_list[2]}\n')
            i += 1