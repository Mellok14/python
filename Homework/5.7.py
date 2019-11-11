import json
with open('text_5.7.1.txt', 'r', encoding='utf-8') as file_1:
    profit = 0
    i = 0
    total_profit = 0
    mid_profit =0
    my_list =[]
    dict_1 = {}
    dict_2 = {}
    for line in file_1:
        list_1 = line.split()
        profit = int(list_1[2]) - int(list_1[3])
        if profit > 0:
            i += 1
            total_profit = total_profit + profit
        dict_1[list_1[0]] = profit
        profit = 0
    mid_profit = total_profit/i
    dict_2['middle_profit'] = round(mid_profit, 2)
    my_list.append(dict_1)
    my_list.append(dict_2)
    with open('text_5.7.2.json', 'w', encoding='utf-8') as file_2:
        json.dump(my_list, file_2, ensure_ascii=False)