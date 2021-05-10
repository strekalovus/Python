class Worker:
    name = None
    surname = None
    position = None
    income = None

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        self.__income = {"wage": self.wage, "bonus": self.bonus}
        return self.__income


manager = Position('Petr', 'Petrov', 'manager', 500, 100)
print(manager.get_full_name(), manager.get_total_income())
