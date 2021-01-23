from abc import ABC, abstractmethod


# Абстрактный базовый класс Одежда
class Clothes(ABC):
    def __init__(self, name='unnamed_clothes'):
        self.name = name

    # Абстрактный метод
    @abstractmethod
    def get_name(self):
        pass


# Дочерний класс Костюм
class Suit(Clothes):
    def __init__(self, growth, name='unnamed_clothes'):
        self.growth = growth
        super(Suit, self).__init__(name=name)

    # Метод рассчёта затратов ткани
    # Объявлен как параметр
    @property
    def cloth_consumption(self):
        return 2 * self.growth + 0.3

    # Переопределение абстрактоного родительсокго метода
    def get_name(self):
        return Suit.__name__ + f': ' + self.name


# Дочерний класс Пальто
class Coat(Clothes):
    def __init__(self, size, name='unnamed_clothes'):
        self.size = size
        super(Coat, self).__init__(name=name)

    # Метод рассчёта затратов ткани
    # Объявлен как параметр
    @property
    def cloth_consumption(self):
        return self.size / 6.5 + 0.5

    # Переопределение абстрактоного родительсокго метода
    def get_name(self):
        return self.name


# Объявление объекта класса Пальто
# вывод пременной объекта, параметра объекта, вызов унаследованного абстрактоного метода
coat_one = Coat(10, 'Coat_one')
print(coat_one.name)
print(coat_one.cloth_consumption)
print(coat_one.get_name())

print(f'-'*30)

# Объявление объекта класса Костюм
# вывод параметра объекта, вызов унаследованного абстрактоного метода
suit_one = Suit(15)
print(suit_one.cloth_consumption)
print(suit_one.get_name())
