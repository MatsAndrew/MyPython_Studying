#task_5

def my_func():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите ваши числа или нажмите Q для выхода из программы ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма ваших чисел равна {sum_res}')
    print(f'Сумма ваших последних числе равна {sum_res}')


my_func()
