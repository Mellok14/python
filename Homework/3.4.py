def my_func1(x,y):
    result = x**y
    return round(result, 9)
print(my_func1(int(input('Enter the positive number: ')), int(input('Enter the negative number of exponent: '))))

def my_func2(x,y):
    exp = 1
    result =1
    while exp <= abs(y):
        result = result*x
        exp +=1
    result = 1/result
    return round(result, 9)
print(my_func2(int(input('Enter the positive number: ')), int(input('Enter the negative number of exponent: '))))