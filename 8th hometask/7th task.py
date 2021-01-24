# Класс Комплексное число
class ComplexNumber:
    # Конструктор: получение вещественной и мнимой частей из параметров
    def __init__(self, part_normal, part_complex):
        # Сохранить вещественную часть
        self.__part_normal = part_normal
        # Сохранить мнимую часть
        self.__part_complex = part_complex

    # Переопределение метода для отображения комплексного числа в строковом формате
    def __str__(self):
        return f'{self.__part_normal} + {self.__part_complex}i'

    # Переопределение метода сложения комплексных чисел
    def __add__(self, other):
        return ComplexNumber(self.__part_normal + other.__part_normal, self.__part_complex + other.__part_complex)

    # Переопределение метода умножения комплексных чисел
    def __mul__(self, other):
        return ComplexNumber(self.__part_normal * other.__part_normal - self.__part_complex * other.__part_complex,
                             self.__part_normal * other.__part_complex + self.__part_complex * other.__part_normal)


# Создание комплексного числа а и его отображение
complex_a = ComplexNumber(1, 2)
print(f'a =\t\t{complex_a}')

# Создание комплексного числа б и его отображение
complex_b = ComplexNumber(3, 4)
print(f'b =\t\t{complex_b}')

# Переопределение комплексного чисола а:
# теперь комплексное число а равно сумме самого себя и комплексного числа б
complex_a = complex_a + complex_b
print(f'a = a + b =\t\t{complex_a}')

# Переопределение комплексного числа б:
# теперь комплексное число б равно произведению самого себя и комплексного чисола а
complex_b = complex_a * complex_b
print(f'b = a * b =\t\t{complex_b}')
