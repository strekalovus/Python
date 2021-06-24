def fact(number):
    count = 1
    while count <= number:
        yield count
        count += 1


i = 1
my_num = []
for el in fact(5):
    if i > 20:
        break
    else:
        my_num.append(el)
        i += 1
print(my_num)
