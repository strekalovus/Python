my_list = ['Audi A5\n', 'BMW 5-series\n', 'Mercedes C-class\n']
with open("my_file_2.txt", 'w') as my_file:
    my_file.writelines(my_list)
with open("my_file_2.txt") as my_file:
    lines = 0
    words = 0
    for line in my_file:
        lines += line.count("\n")
        words = len(line.split())
        print(f"Количество слов в строке - {words}")
    print(f"Количество строк - {lines}")
