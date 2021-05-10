a = int(input("Введите делимое целое число: "))
b = int(input("Введите целое число делитель: "))


def my_func(dividend, divisor):
    if divisor == 0:
        quotient = 0
    else:
        quotient = dividend / divisor
    return quotient


result = my_func(a, b)
print(result)
