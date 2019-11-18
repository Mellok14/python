from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    @abstractmethod
    def calculate(self):
        return 'Method of parent class'
class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
    @property
    def calculate(self):
        return round(self.param/6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
    @property
    def calculate(self):
        return round(self.param*2 + 0.3, 2)


my_coat = Coat(10)
print(my_coat.calculate)

my_suit = Suit(10)
print(my_suit.calculate)