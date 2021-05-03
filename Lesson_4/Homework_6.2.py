from itertools import cycle


def my_func(my_list, iteration):
    i = 0
    iterator = cycle(my_list)
    while i < iteration:
        print(next(iterator))
        i += 1


my_func(my_list=[1, 2], iteration=int(input("Введите количество итераций: ")))


