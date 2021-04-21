start = int(input('Введите начальный показатель в км: '))
finish = int(input('Введите цель в км: '))
day = 1
while start < finish:
    start = start * 1.1
    day = day + 1
print(day)
