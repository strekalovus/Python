index = 1
result = []
spec = ["Наименование", "Стоимость", "Количество", "Сумма"]

while True:
    question = input("Вы хотите добавить новый товар (да/нет)? ")
    if question.upper() == "НЕТ":
        break
    item = {}

    for spe in spec:
        user_data = input(f"Введите {spe} ")
        if user_data.isdigit():
            item[spe] = int(user_data)
        else:
            item[spe] = user_data
    result.append(tuple([index, item]))
    index = index + 1

print(result)

res_dict = {}

for item in spec:
    for _, param in result:
        if res_dict.get(item):
            res_dict[item].append(param.get(item))
        else:
            res_dict[item] = [param.get(item)]

print(res_dict)
