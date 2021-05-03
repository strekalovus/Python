import random

my_list = [random.randint(1, 100) for _ in range(20)]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(my_list)
print(new_list)
