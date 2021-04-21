time = int(input("Введите время в секундах: "))
sec = time % 60
minute = (time - sec) // 60
hour = minute // 60
minute = minute % 60
if sec == 0:
    sec = '00'
if minute == 0:
    minute = '00'
if hour == 0:
    hour = '00'
print(f'{hour}:{minute}:{sec}')
