result = 0
while True:
    line = input("Введите число или специальный символ 'e': ")
    symbols = line.split(" ")
    for symbol in symbols:
        try:
            number = float(symbol)
            result = result + number
        except ValueError:
            if symbol == 'e':
                print(f"Сумма введённых чисел {result}.")
                exit()



