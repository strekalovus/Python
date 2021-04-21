num = int(input('Введите целое число: '))
rem = num % 10
num = num // 10
while num > 1:
    if num % 10 > rem:
        rem = num % 10
    num = num // 10
print(rem)
