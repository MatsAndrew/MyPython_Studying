# task_5

profit = float(input("Укажите выручку вашей фирмы: "))
taxes = float(input("Укажите ваши издержки: "))
if profit > taxes:
    print(f"Ваша фирма работает с прибылью. Рентабельность выручки: {profit / taxes:.2f}")
    staff = int(input("Укажите количество сотрудников вашей фирмы: "))
    print(f"Прибыль в расчете на одного сотрудника: {profit / staff:.2f}")
elif profit == taxes:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")