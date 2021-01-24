# task_6

a = int(input("Результат первого дня тренировок в км: "))
b = int(input("Желаемый результат в км: "))
result_day = 1
while a < b:
    a *= 1.1
    result_day += 1
print("День достижения цели: %.d" % result_day)