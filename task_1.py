# task_1

def my_func():
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "Делитель не должен равняться нулю!"
    except ValueError:
        return "Введите только число"


print(my_func())
