def calc_pay(a, b, c):
    pay = a * b + c
    return pay


hour = float(input('Введите количество отработанных часов: '))
rate = float(input('Введите сумму оплаты труда за 1 час: '))
bonus = float(input('Введите размер премии: '))
final_pay = calc_pay(hour, rate, bonus)
print(f'Размер заработной платы составляет: {final_pay}')
