my_list = []
while True:
    text = input("Введите текст: ")
    if text == '':
        print(my_list)
        exit()
    else:
        new_text = text + '\n'
        my_list.append(new_text)
    with open("my_file.txt", "w") as file_obj:
        file_obj.writelines(my_list)
