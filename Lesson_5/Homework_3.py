team = {'Иванов': 17000, 'Петров': 15000, 'Сидоров': 25000}
try:
    my_file = open("my_file_3.txt", 'w')
    for name, salary in team.items():
        my_file.write(name + ':' + str(salary) + "\n")
finally:
    my_file.close()

amount = 0
count = 0
group = []
with open("my_file_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tag = line.split(':')
        if int(tag[1]) < 20000:
            group.append(tag[0])
        amount += int(tag[1])
        count += 1
result = amount / count
print(f"Сотрудники с окладом меньше 20 000: {group}")
print(f"Средний оклад сотрудников: {result}")
