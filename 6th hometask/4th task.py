# Определение класса Машина
class Car:
    # Получение атрибутов из аргументов:
    # name          - имя машины, обязательный аргумент
    # color         - цвет машины, необязательный аргумент, по умолчанию чёрный
    # speed         - скорость машины, необязательный аргумент, по умолчанию 0 км/ч
    # is_police     - принадлежность к полиции, необязательный аргумент, по умолчанию Нет
    def __init__(self, name, color='Black', speed=0, is_police=False):
        self.name, self.color, self.speed, self.is_police = name, color, speed, is_police
        self.direction = None

    # Метод Поехать
    # может принимать аргумент скорость
    # если аргумент не указан, то используется текущее значение скорости
    def go(self, speed=None):
        if speed is not None:
            self.speed = speed
        print(f'{self.name} is driving {self.speed} kmph')

    # Метод Остановиться
    def stop(self):
        self.speed = 0
        print(f'{self.name} has stopped, 0 kmph')

    # Метод Повернуть
    # обязательный аргумент направление
    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} has turned to {self.direction}')

    # Метод Показать скорость
    def show_speed(self):
        print(f'{self.name}s speed is {self.speed} kmph')


# Определение класса Городская машина
class TownCar(Car):
    # Приватная переменная для хранения разрешённой скорости
    _allowed_speed = 60

    # Переопределение метода Показать скорость
    def show_speed(self):
        # Если скорость меньше максимальной разрешённой скорости
        if self.speed <= self._allowed_speed:
            # то отобразить скорость
            print(f'{self.name}s speed is {self.speed} kmph')
        # иначе
        else:
            # отобразить скорость и предупреждение
            print(f'{self.name}s speed is {self.speed} kmph. '
                  f'Exceeded legal amount on {self.speed - self._allowed_speed} kmph!')


# Определение класса Спортивная машина
class SportCar(Car):
    pass


# Определение класса Рабочая машина
class WorkCar(TownCar):
    # Приватная переменная для хранения разрешённой скорости
    _allowed_speed = 40

    def aaa(self):
        print(self._allowed_speed)


# Определение класса Полицейская машина
class PoliceCar(Car):
    # Переопределение конструктора
    # теперь значение аргумента is_police по умолчание True
    def __init__(self, name, color, speed=0, is_police=True):
        # обращение к конструктору родительского класса для сохранения атрибутов
        super(PoliceCar, self).__init__(name, color, speed, is_police)


print(f'\n', f'_'*30)
# Создание объекта класса Машина и вызов метода Повернуть
new_car = Car('New_car', 'Red', 40)
new_car.turn('Park')

print(f'\n', f'_'*30)
# Создание объекта класса Полицейская машина и вызов метода Остановиться
new_police_car = PoliceCar('New_police_car', 'Blue')
new_police_car.stop()

print(f'\n', f'_'*30)
# Создание объекта класса Рабочая машина и вызов методов Поехать и Показать скорость
new_work_car = WorkCar('New_work_car')
new_work_car.go(50)
new_work_car.show_speed()
new_work_car.aaa()

print(f'\n', f'_'*30)
# Создание объекта класса Городская машина и вызов методов Остановиться и Показать скорость
new_town_car = TownCar('New town car', 'Green', 70, True)
new_town_car.show_speed()
new_town_car.stop()
new_town_car.show_speed()
