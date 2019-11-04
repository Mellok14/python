def my_func(arg_1,arg_2,arg_3):
    sum_max = arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    return sum_max
print(my_func(int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: '))))

