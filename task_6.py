# task_6

from itertools import count
from itertools import cycle


for el in count(3):
    if el == 10:
        break
    else:
        print(int(el))

c = 0
for el in cycle("шалаш "):
    if c > 20:
        break
    print(el)
    c += 1
