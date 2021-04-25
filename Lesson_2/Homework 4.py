my_str = input("Введите текст: ")
list = my_str.split(' ')
for index, element in enumerate(list, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{index}. {element}")