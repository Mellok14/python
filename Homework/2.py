time = int(input('Enter the time in seconds: '))
hour = time // 3600
minute = (time % 3600)//60
second = (time % 3600)%60
print(f'{hour}:{minute}:{second}')