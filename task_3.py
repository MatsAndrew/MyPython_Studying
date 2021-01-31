#task_3

def my_func(a, b, c):
    if a > b and c > b:
        return a + c
    elif b > a and c > a:
        return b + c
    elif a > c and b > c:
        return a + b


print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье '
                                                                                                    'число: '))))
