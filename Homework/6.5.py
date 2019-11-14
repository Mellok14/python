class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')
class Pen:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки, используется {self.title}')
class Pencil:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки, используется {self.title}')
class Handle:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки, используется {self.title}')

pen_1 = Pen('ручка')
pen_1.draw()
pencil_1 = Pencil('карандаш')
pencil_1.draw()
handle_1 = Handle('маркер')
handle_1.draw()