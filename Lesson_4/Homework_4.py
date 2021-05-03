import random

my_list = [random.randint(1, 44) for _ in range(14)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new_list)
