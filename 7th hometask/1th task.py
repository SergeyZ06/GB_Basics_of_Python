import random


# Класс Матрица
class Matrix:

    # Получение списка списков из аргумента при помощи конструктора
    def __init__(self, arg):
        self.matrix_list = arg

    # Перегрузка метода для вывода матрицы как строки
    def __str__(self):
        # Строка для формирования нового отображения матрицы
        str_return = ''

        # Для каждой строки матрицы
        for y in self.matrix_list:
            # для каждого элемента в строке
            for x in y:
                # записать значение элемента с отступом
                str_return += f'{x}\t'
            # сделать перенос строки после окончания строки матрицы
            str_return += f'\n'

        # Вернуть строку с новым отображением матрицы
        return str_return

    # Перегрузка метода сложения матрицы
    def __add__(self, other):
        # Список для хранения элементов новой матрицы
        new_matrix = []

        # Для каждых строк слагаемых матриц
        for index_y, value_y in enumerate(other):
            # добавить новый элемент - пустой список для последующей записи новых элементов
            new_matrix.append([])
            # для каждых элементов слагаемых матриц
            for index_x, value_x in enumerate(value_y):
                # добавить в список новой матрицы вычисленный элемент
                new_matrix[index_y].append(self.matrix_list[index_y][index_x] + value_x)

        # Вернуть новую вычисленную матрицу
        return Matrix(new_matrix)

    # Перегрузка для метода для возможности итерировать содержимое матрицы
    def __iter__(self):
        return iter(self.matrix_list)


# Создание объектов класса Матрица
matrix_1 = Matrix([[random.randint(0, 9), random.randint(0, 9)], [random.randint(0, 9), random.randint(0, 9)]])
matrix_2 = Matrix([[random.randint(0, 9), random.randint(0, 9)], [random.randint(0, 9), random.randint(0, 9)]])

# Отображение содержимого объектов
print(matrix_1)
print(matrix_2)

# Создание нового объекта Матрица в результате сложения существующих объектов
matrix_3 = matrix_1 + matrix_2

# Отображение содержимого нового объекта
print(matrix_3)
