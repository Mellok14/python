class Complex:
  def __init__(self, real_path, complex_path):
    self.number = complex(real_path, complex_path)
  def __add__(self, other):
    return self.number + other.number
  def __mul__(self, other):
    return self.number*other.number

c_1 = Complex(3, 4)
c_2 = Complex(2, 2)

print(c_1 + c_2)
print(c_1*c_2)