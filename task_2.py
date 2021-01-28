# task_2

lst = list(input('Введите элементы списка без пробела: '))
a = 0
for i in range(int(len(lst)/2)):
    lst[a], lst[a+1] = lst[a+1], lst[a]
    a += 2

print(lst)
