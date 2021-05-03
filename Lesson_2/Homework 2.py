my_list = [1, 2, 3, 4, 5, 6, 7]
if len(my_list) % 2 == 0:
    index = 0
    while index < len(my_list):
        element = my_list[index]
        my_list[index] = my_list[index + 1]
        my_list[index + 1] = element
        index = index + 2
else:
    index = 0
    while index < len(my_list) - 1:
        element = my_list[index]
        my_list[index] = my_list[index + 1]
        my_list[index + 1] = element
        index = index + 2
print(my_list)
