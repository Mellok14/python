my_list = [1, 3, 2, 5, 8, 9, 22, 20, 48, 66, 50, 9]
new_list = [el for i, el in enumerate(my_list) if int(el) > int(my_list[i - 1])]
print(new_list)
