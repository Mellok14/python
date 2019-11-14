class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        print(f'Full name of worker: {self.name} {self.surname}')
    def get_total_income(self):
        total_income = 0
        total_income = self.income['wage'] + self.income['bonus']
        print(total_income)

worker_1 = Position('Alex', 'Smith', 'engeneer', 10000, 2000)
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
worker_1.get_full_name()
worker_1.get_total_income()