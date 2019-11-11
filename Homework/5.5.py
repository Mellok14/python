import random
total = 0
s = ''
with open('text_5.5.txt', 'w') as file:
        for i in range(1,10):
            file.write(f'{random.randint(1,50)} ')
with open('text_5.5.txt', 'r') as file_1:
        s = file_1.read()
        total = sum(map(int, s.split()))
print(total)