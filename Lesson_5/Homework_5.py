my_file = open("my_file_5.txt", 'w')
text = my_file.write("1 2 3 4 5 6 7 8")
my_file.close()

my_file = open("my_file_5.txt", 'r')
content = my_file.readline()

tag = content.split()
summa = 0
for i in tag:
    summa = summa + int(i)

print(summa)



