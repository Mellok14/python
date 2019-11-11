with open('text_5.1.txt', 'w') as f:
     my_str = input('Введите данные для записи, для завершения записи нажмите Enter:')
     while my_str != '':
            f.write(my_str + "\n")
            my_str = input('Введите данные для записи, для завершения записи нажмите Enter:')