# Определение класса Работник
class Worker:
    # Словарь для хранения соответствия должности и зарплаты, премии
    # 'Должность': спиок(зарплата, премия)
    __dict_worker_wage = {
        'Junior': (30000, 15000),
        'Middle': (50000, 25000),
        'Senior': (75000, 50000)
    }

    # Получение атрибутов при инициализации объекта, вычисление дохода в соотвествии с должностью
    def __init__(self, name, surname, position='Junior'):
        # Получение атрибутов из аргументов
        self.name, self.surname, self.position = name, surname, position
        # Вычисление дохода при помощи обращения к словарю
        self._wage = self.__dict_worker_wage.get(self.position)[0] + self.__dict_worker_wage.get(self.position)[1]


# Дочерний класс Должность
class Position(Worker):
    # Метод получения полного имени сотрудника
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    # Метод получения дохода сотрудника
    def get_total_income(self):
        return self._wage


# Создание объектов класса Должность
position_01 = Position('Ivan', 'Ivanov')
position_02 = Position('Petr', 'Petrov', 'Middle')

# Отображение полных имён объектов
print(position_01.get_full_name())
print(position_02.get_full_name())

# Отображение доходов объектов
print(position_01.get_total_income())
print(position_02.get_total_income())
