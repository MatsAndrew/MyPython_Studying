# task_3

seasons_lst = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input('Введите номер месяца: '))
if month ==1 or month ==2 or month ==12:
    print(seasons_dict.get(1))
    print(seasons_lst[0])

elif month ==3 or month ==4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_lst[1])

elif month ==6 or month ==7 or month ==8:
    print(seasons_dict.get(3))
    print(seasons_lst[2])

elif month ==9 or month ==10 or month ==11:
    print(seasons_dict.get(4))
    print(seasons_lst[3])

else:
    print('Вы ошиблись при введении номера месяца')
