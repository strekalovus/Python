interpreter = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []

try:
    my_file = open("my_file_4.1.txt", 'r')
    for line in my_file:
        tag = line.split(" - ")
        print(tag)
        if tag[0] in interpreter:
            word = interpreter[tag[0]]
            result.append(word + ' - ' + tag[1])
    print(result)
finally:
    my_file.close()

try:
    new_file = open("my_file_4.2.txt", "w")
    new_file.writelines(result)
finally:
    new_file.close()
