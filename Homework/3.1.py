def division(arg_1, arg_2):
    try:
        div = round(arg_1/arg_2, 3)
        return div
    except ZeroDivisionError:
        return 'Division by zero!'
print(division(int(input('Enter first number: ')),int(input('Enter second number: '))))