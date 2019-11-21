class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
class Warehouse:
    dict_printer = {'Name:': [], 'Quantity:': [], 'Color:': []}
    dict_scanner = {'Name:': [], 'Quantity:': [], 'Hand_held:': []}
    dict_xerox = {'Name:': [], 'Quantity:': [], 'Mass:': []}
    @classmethod
    def add_printer(cls, *args):
        for el in args:
            try:
                if str(el.quantity).isdigit() == False:
                    raise OwnError('Quantity must be a number, this item will be excluded from the database!!!')
            except OwnError as err:
                print(err)
            else:
                Warehouse.dict_printer['Name:'].append(el.name)
                Warehouse.dict_printer['Quantity:'].append(el.quantity)
                Warehouse.dict_printer['Color:'].append(el.color)
    @classmethod
    def add_scanner(cls, *args):
        for el in args:
            try:
                if str(el.quantity).isdigit() == False:
                    raise OwnError('Quantity must be a number, this item will be excluded from the database!!!')
            except OwnError as err:
                print(err)
            else:
                Warehouse.dict_scanner['Name:'].append(el.name)
                Warehouse.dict_scanner['Quantity:'].append(el.quantity)
                Warehouse.dict_scanner['Hand_held'].append(el.hand_held)
    @classmethod
    def add_xerox(cls, *args):
        for el in args:
            try:
                if str(el.quantity).isdigit() == False:
                    raise OwnError('Quantity must be a number, this item will be excluded from the database!!!')
            except OwnError as err:
                print(err)
            else:
                Warehouse.dict_xerox['Name:'].append(el.name)
                Warehouse.dict_xerox['Quantity:'].append(el.quantity)
                Warehouse.dict_xerox['Mass:'].append(el.mass_kg)
    @classmethod
    def get_info_printer(cls):
        return '\nName:     ' + '\t'.join(map(str, Warehouse.dict_printer['Name:'])) + \
               '\nQuantity: ' + '\t'.join(map(str, Warehouse.dict_printer['Quantity:'])) + \
               '\nColor:    ' + '\t'.join(map(str, Warehouse.dict_printer['Color:'])) + \
                '\nTotal quantity of equipment: ' + str(sum(Warehouse.dict_printer['Quantity:']))
    @classmethod
    def get_info_scanner(cls):
        return '\nName:     ' + '\t'.join(map(str, Warehouse.dict_printer['Name:'])) + \
               '\nQuantity: ' + '\t'.join(map(str, Warehouse.dict_printer['Quantity:'])) + \
               '\nHand_held:' + '\t'.join(map(str, Warehouse.dict_printer['Hand_held:'])) + \
                '\nTotal quantity of equipment: ' + str(sum(Warehouse.dict_printer['Quantity:']))
    @classmethod
    def get_info_xerox(cls):
        return '\nName:     ' + '\t'.join(map(str, Warehouse.dict_printer['Name:'])) + \
               '\nQuantity: ' + '\t'.join(map(str, Warehouse.dict_printer['Quantity:'])) + \
               '\nMass:     ' + '\t'.join(map(str, Warehouse.dict_printer['Mass:'])) + \
                '\nTotal quantity of equipment: ' + str(sum(Warehouse.dict_printer['Quantity:']))
class Office_equipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
class Printer(Office_equipment):
    def __init__(self, name, quantity, color):
        super().__init__(name, quantity)
        self.color = color
class Scanner(Office_equipment):
    def __init__(self, name, quantity, hand_held):
        super().__init__(name, quantity)
        self.hand_held = hand_held
class Xerox(Office_equipment):
    def __init__(self, name, quantity, mass_kg):
        super().__init__(name, quantity)
        self.mass_kg = mass_kg

print_1 = Printer('XEROX', 3, True)
print_2 = Printer('Kiocera', 'i', False)
scan_1 = Scanner('OKI', 10, False)
scan_2 = Scanner('Sony', 11, True)
xerox_1 = Xerox('HP', 7,  23)
xerox_2 = Xerox('Philips', 3, 18)
Warehouse.add_printer(print_1, print_2)
Warehouse.add_xerox(xerox_1, xerox_2)
print(Warehouse.get_info_printer())
