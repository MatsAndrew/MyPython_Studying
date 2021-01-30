#task_6

products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

index = len(products) + 1

while True:
    menu = input('Нажмите p, чтобы добавить продукт\nНажмите a, чтобы посмотреть аналитику\nНажмите q, чтобы выйти из программы\n')
    if menu == 'p':
        name, price, count, unit = input('Введите через пробел название, цену, кол-во, единицу измерения: ').split()
        products.append((
            index,
            {
                'название': name,
                'цена': int(price),
                'количество': int(count),
                'eд': unit,
            }
        ))
        index += 1
    elif menu == 'a':
        res = {
            'название': set(),
            'цена': set(),
            'количество': set(),
            'eд': set(),
        }
        for product in products:
            res['название'].add(product[1]['название'])
            res['цена'].add(product[1]['цена'])
            res['количество'].add(product[1]['количество'])
            res['eд'].add(product[1]['eд'])
        print(res)
    elif menu == 'q':
        break