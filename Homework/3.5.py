summa = 0
try:
    while True:
        for n in map(int, input('Введите ряд чисел через пробел, для завершения введите "Q"').split()):
            summa += n
        print(summa)
except ValueError:
    print('Итоговый результат: ', summa)