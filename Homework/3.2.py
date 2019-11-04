def contaсt(**kwargs):
    print('; '.join('{} is {}'.format(key, value) for key, value in kwargs.items()))
name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
birth_year = input('Enter your year of birth: ')
town = input('Enter your city of residence: ')
email = input('Enter your email: ')
number = input('Enter your phone number: ')
contaсt(firstname=name, lastname=last_name, birth_year=birth_year, city=town, email=email, phone_number=number)