def int_func(arg_1):
    return arg_1.capitalize()
my_str = ''
new_str = ''
while my_str != 'Q':
    my_str = input('Введите ряд слов через пробел, для завершения введите "Q"')
    for i in my_str.split():
        new_str = new_str + ' ' + int_func(str(i))
    print(new_str)
    new_str = ''
