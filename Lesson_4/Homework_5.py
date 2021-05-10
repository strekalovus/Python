from functools import reduce

data = range(100, 1001)
new_data = [el for el in data if el % 2 == 0]
mul_all = reduce(lambda x, y: x + y, new_data)
print(mul_all)
