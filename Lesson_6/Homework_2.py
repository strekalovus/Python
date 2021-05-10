class Road:
    __length = None
    __width = None
    weight = None
    thick = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def expense(self):
        self.weight = 25
        self.thick = 5
        expense = self.length * self.width * self.weight * self.thick / 1000
        print(f'Необходимо {expense} тонн асфальта')


new_road = Road(5000, 20)
new_road.expense()
