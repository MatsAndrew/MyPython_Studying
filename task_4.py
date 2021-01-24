# task_4

x = int(input("Целое положительное число: "))
max = x % 10
while x >= 1:
    x = x // 10
    if x % 10 > max:
        max = x % 10
    if x > 9:
        continue
    else:
        print('Самая большая цифра в числе: ', max)
        break