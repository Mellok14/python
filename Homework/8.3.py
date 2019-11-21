class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
list_of_number = []
number = 0
try:
    number = input('Введите число')
    while number != '':
        if number.isdigit() == False and number != '':
            print(OwnError("Это не число"))
        else: list_of_number.append(number)
        number = input('Введите число')
finally:
    print(list_of_number)
