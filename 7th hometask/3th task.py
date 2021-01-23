# Класс Клетка
class Cell:
    def __init__(self, number_of_cells):
        # Переменная для хранения кол-ва клеток в объекте Клетка
        self.number_of_cells = number_of_cells

    # Переопределение метода Сложение
    # возвращает новую клетку, кол-во клеток новой клетки равно сумме клеток в слагаемых слетках
    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    # Переопределение метода Вычитание
    # возвращает новую клетку, кол-во клеток новой клетки равно разности указанных клеток
    # выводит сообщение об ошибке, в случае если кол-во клеток новой клетки получается отрицательным
    def __sub__(self, other):
        if self.number_of_cells < other.number_of_cells:
            print(f'Error: number of cells would be below zero.')
            return None
        else:
            return Cell(self.number_of_cells - other.number_of_cells)

    # Переопределение метода Умножение
    # возвращает новую клетку, кол-во клеток новой клетки равно произведению указанных клеток
    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    # Пееопределение метода Деление
    # возвращает новую клетку, кол-во клеток новой клетки равно частному от деления указанных клеток
    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    # Метод отображение ячеек по рядам
    # возвращает строку, содержащую ячейки, разделённую на ряды
    def make_order(self, number_of_cells_in_row=1):
        # Переменная для хранения ячеек (*)
        # изначально все ячейки хранятся в одном ряду
        str_to_return = f'*' * self.number_of_cells
        # Счётчик для деления изначального ряда на необходимое кол-во рядов
        i = 0
        # Пока счётчик меньше необходимого кол-ва рядов
        while i < self.number_of_cells // number_of_cells_in_row:
            # Вычислить позицию для разделения
            position = number_of_cells_in_row * (i + 1) + i
            # Добавить символ разделения строки на вычисленную позицию
            str_to_return = str_to_return[:position] + f'\n' + str_to_return[position:]
            i += 1

        return str_to_return

    # Попытка обработать исключение при обращении к Клетке, в случае вычитания с отрицательным результатом
    # Не получилось, так как в переменную записывается не ссылка на новый объект без параметра, а ссылка на None
    # Поэтому обрабатывать исключение пришлось в коде программы
    def __getattr__(self, item):
        if item == self.number_of_cells:
            try:
                return self.number_of_cells
            except AttributeError:
                return f'Current cell do not have attribute "number_of_cells".' \
                       f'Maybe some error has occurred during creating this cell'


# Объявление двух объектов класса Клетка
print(f'\n')

new_cell_one = Cell(5)
print(f'New cell one has {new_cell_one.number_of_cells} cells')

new_cell_two = Cell(10)
print(f'New cell two has {new_cell_two.number_of_cells} cells')


# Сложение клеток
print(f'\n')

new_cell_three = new_cell_one + new_cell_two
print(f'The result of summing New cell one and New cell two is New cell three,'
      f' which has {new_cell_three.number_of_cells} cells')


# Попытка вычитания клеток с отрицательным результатом
print(f'\n')

new_cell_three = new_cell_one - new_cell_two
try:
    print(new_cell_three.number_of_cells)
except AttributeError:
    print(f'New cell has not been formed because of the error above.')


# Вычитание клеток
print(f'\n')

new_cell_three = new_cell_two - new_cell_one
print(f'The result of subtracting New cell two minus New cell one is New cell three,'
      f' which has {new_cell_three.number_of_cells} cells')


# Умножение клеток
print(f'\n')

new_cell_three = new_cell_one * new_cell_two
print(f'The result of multiplying New cell one and New cell two is New cell three,'
      f' which has {new_cell_three.number_of_cells} cells')


# Деление клеток
print(f'\n')

new_cell_three = new_cell_two / new_cell_one
print(f'The result of division New cell two on New cell one is New cell three,'
      f' which has {new_cell_three.number_of_cells} cells')


# Вывод ячеек клетки по рядам, 3 ячейки в ряду
print(f'\n')

print(f'The result of separating New cell two on rows, with three cells per each row:')
print(new_cell_two.make_order(3))


# Вывод ячеек клетки по рядам, 12 ячейки в ряду
print(f'\n')

print(f'The result of separating New cell four, which has 100 cells, on rows, with twelve cells per each row:')
new_cell_four = Cell(100)
print(new_cell_four.make_order(12))
