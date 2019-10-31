product ={}
product_tup = ()
product_list = []
i = 1
while True:
    product = {'название': input('Введите название товара'), 'цена': int(input('Введите стоимость: ')), 'количество': int(input('Введите количество: ')), 'eд': input('Введите еденицу измерения: ')}
    product_tup = (i, product)
    i += 1
    product_list.append(product_tup)
    product ={}
    info = input('Напишите знак "+" если хотите продолжить: ')
    if info != '+':
        break
print(product_list)
print('Сводная аналитика:')
analiz_dict = {}
name = []
price = []
quantity = []
unit = []
for i in product_list:
    name.append(i[1]['название'])
    price.append(i[1]['цена'])
    quantity.append(i[1]['количество'])
    unit.append(i[1]['eд'])
analiz_dict = {'название': name, 'цена': price , 'количество': quantity, 'eд': unit}
print(analiz_dict)

