class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num
    def make_order(self, cell_in_row):
        if self.cell_num > 0:
            return ('\n%s' % ('*'*cell_in_row))*(self.cell_num//cell_in_row) + '\n%s' % ('*'*(self.cell_num%cell_in_row))
        else:
            return 'Incorrect value of cell for this operation'
    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)
    def __sub__(self, other):
        return Cell(self.cell_num - other.cell_num)
    def __mul__(self, other):
        return Cell(self.cell_num*other.cell_num)
    def __truediv__(self, other):
        return Cell(int(round(self.cell_num/other.cell_num,0)))

my_cell_1 = Cell(16)
print(my_cell_1.make_order(3))
my_cell_2 = Cell(8)
print(my_cell_2.make_order(4))
print((my_cell_1+my_cell_2).make_order(6))
print((my_cell_1-my_cell_2).make_order(6))
print((my_cell_1*my_cell_2).make_order(12))
print((my_cell_1/my_cell_2).make_order(1))
