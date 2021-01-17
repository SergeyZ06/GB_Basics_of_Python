# Определение класса Дорога
class Road:
    # Вызор конструктора для получения атрибутов объекта
    # Два обяательных аргумента:
    # length    - длина дороги
    # width     - ширина дороги
    def __init__(self, length, width):
        # Запись значений агументов в атрибуты объекта
        self._length, self._width = length, width

    # Метод Получить стоимость асфальтирования дороги
    # Два необязательных аргумента:
    # square_cost   - затраты на единицу площади
    # layers        - кол-во слоёв асфальтирования
    def get_cover_costs(self, square_cost=1.0, layers=1):
        # Вернуть вычисленную стоимость асфальтирования дороги
        return f'Asphalt weight: {self._length * self._width * square_cost * layers}'


# Создание объекта класса Дорога
new_road = Road(1000, 10)
# Вывод результата работы метода
print(new_road.get_cover_costs(2.5))

# Тоже самое
yet_another_road = Road(5000, 20)
print(yet_another_road.get_cover_costs(25, 5))
