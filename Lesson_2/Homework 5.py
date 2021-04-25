number = int(input("Введите целое число: "))
my_list = [7, 5, 3, 3, 2]
my_list.append(number)
my_list = sorted(my_list)
my_list.reverse()
print(my_list)
