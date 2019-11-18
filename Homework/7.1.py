class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.my_list])
    def __add__(self, other):
        new_list = []
        i = 0
        for list in self.my_list:
            new_list.append([x + y for x, y in zip(list, other.my_list[i])])
            i += 1
        return Matrix(new_list)

matx_1 = Matrix([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(matx_1)
print('___________')
matx_2 = Matrix([[1,2,3], [1, 1, 1], [2, 2, 2]])
print(matx_2)
print('___________')
print(matx_1+matx_2)