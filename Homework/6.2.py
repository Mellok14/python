class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def mass(self):
        mas = self._length*self._width*25*5
        print(round(mas/1000, 1))
road_1 = Road(20, 5000)
road_1.mass()