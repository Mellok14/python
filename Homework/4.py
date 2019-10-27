number = int(input('Enter number: '))
max_number = number%10
while number > 0:
    number = number // 10
    if number%10 > max_number:
        max_number = number%10
print(max_number)