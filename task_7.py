# task_7

from math import factorial
from itertools import count


def generator(n):
    for el in count():
        yield factorial(el)


fact = generator(6)

for el in fact:
    if el > 6:
        break

    print(el)
