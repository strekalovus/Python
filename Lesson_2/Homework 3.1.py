# через list
month = int(input("Введите номер месяца: "))
month_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
for index, el in enumerate(month_list):
    if index == month - 1:
        print(f"Время года {month_list[index]}")
        break
