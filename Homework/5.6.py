with open('text_5.6.txt', 'r', encoding= 'utf-8') as file:
    my_dict ={}
    s = 0
    digit = ''
    for line in file:
        for k in line.split():
            digit = ''.join(x for x in k if x.isdigit())
            if digit.isdigit():
                s = s + int(digit)
        my_dict[line.split()[0]] = s
        s = 0
    print(my_dict)