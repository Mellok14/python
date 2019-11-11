with open('text_5.3.txt', 'r') as file:
    mid_sel = 0
    sel = 0
    i = 0
    for line in file:
        sel = sel + int(line.split()[1])
        i+=1
        if int(line.split()[1]) < 20000:
            print(f'Worker {line.split()[0]} has salary less than 20000')
    mid_sel = (sel/i)
    print(f'Middle salary {round(mid_sel, 1)}')