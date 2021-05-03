from itertools import count


def my_func(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


my_func(start=int(input("Введите стартовый номер: ")), stop=int(input("Введите конечный номер: ")))
