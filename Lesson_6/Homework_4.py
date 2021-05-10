class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return "Автомобиль поехал"

    def stop(self):
        return "Автомобиль остановился"

    def turn(self, direction):
        return "Автомобиль повернул в " + direction


class TownCar(Cars):
    family = None

    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


audi = TownCar('Audi', 60, 'чёрный')
print(audi.name, audi.color, audi.speed, audi.is_police)
print(audi.go(), audi.turn('город'), audi.stop())
