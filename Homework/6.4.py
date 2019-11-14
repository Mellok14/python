class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
    def go(self):
        print('Car is moving')
    def stop(self):
        print('Car stopped')
    def turn(self, direction):
        self.direction = direction
        print(f'Car turn {self.direction}')
    def show_speed(self):
        print(f'Speed: {self.speed}')
class TownCar(Car):
    is_police = False
    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 60:
            print('Reduce speed!!!')
class SportCar(Car):
    is_police = False
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
class WorkCar(Car):
    is_police = False
    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 40:
            print('Reduce speed!!!')
class PoliceCar(Car):
    is_police = True
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

car_1 = TownCar(62, 'red', 'Peugeot')
print(car_1.is_police)
print(car_1.color)
print(car_1.name)
car_1.show_speed()

car_2 = PoliceCar(62, 'green', 'Opel')
print(car_2.is_police)
print(car_2.color)
print(car_2.name)
car_2.go()
car_2.stop()
car_2.turn('left')
car_2.show_speed()


