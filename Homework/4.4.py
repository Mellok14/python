my_list = [1, 2, 20, 48, 7 , 1, 4, 33, 76, 20, 4, 11, 21, 4, 78, 31, 83, 7]
new_list =[el for el in my_list if my_list.count(el) == 1 ]
print(new_list)