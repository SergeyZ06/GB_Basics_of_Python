from random import randint


# Класс Дата
class Date:
    # Словарь для преобразования списка с частями даты в словарь с частями даты
    dict_parts_of_date = {
        0: 'day',
        1: 'month',
        2: 'year'
    }

    # Конструктор: записывает дату из параметра в атрибут объекта
    def __init__(self, str_data='01-01-1900'):
        dict_date = Date.date_to_numeric(str_data)
        dict_date = self.date_validation(dict_date)

        for index in Date.dict_parts_of_date.keys():
            if dict_date[Date.dict_parts_of_date[index]] is None:
                print(f'Object "{str_data}" was not created successfully')
                print(f'Part "{Date.dict_parts_of_date[index]}" of "{str_data}" is not correct')
                self.dict_date = None
                break
            else:
                self.dict_date = dict_date

        if self.dict_date is not None:
            print(f'Object "{str_data}" was created successfully')

    # Метод Преобразования строчной записи даты в словарь с частями даты
    # Принимает в качестве параметра строковую запись даты
    # Возвращает словарь с частями дат в формате чисел или значение None в случае невозможности преобразования
    @classmethod
    def date_to_numeric(cls, str_to_int):
        # Строка для промежуточного хранения частей даты через пробел
        str_to_int = str_to_int.replace('-', ' ')
        # Словарь для хранения чатей дат, туда будет записан результат работы метода
        dict_to_int = {}
        # Для каждого номера элемента и значения среди списка слов строки (частей даты)
        for index, value in enumerate(str_to_int.split()):
            # пробовать
            try:
                # добавить в итоговый словарь с соотвествующим индексом:
                # 0 - день
                # 1 - месяц
                # 2 - год
                # преобразованную в число соответствующую часть даты
                dict_to_int[cls.dict_parts_of_date.get(index)] = int(value)
            # при невозможности преобразования
            except ValueError:
                # поместить в словарь значение None
                dict_to_int[cls.dict_parts_of_date.get(index)] = None
        # Вернуть сформированный словарь
        return dict_to_int

    # Метод Проверки даты
    # Принимает в качестве параметра строковую запись даты
    @staticmethod
    def date_validation(dict_to_validate):
        # Пробовать
        try:
            # оценить часть даты "День"
            if dict_to_validate['day'] < 1 or dict_to_validate['day'] > 31:
                # в случае некорректного значения убрать значение
                dict_to_validate['day'] = None
        # в случае невозможности сравнения
        except TypeError:
            # убрать значение
            dict_to_validate['day'] = None

        # Аналогичная проверка для части даты "Месяц"
        try:
            if dict_to_validate['month'] < 1 or dict_to_validate['month'] > 12:
                dict_to_validate['month'] = None
        except TypeError:
            dict_to_validate['month'] = None

        # Аналогичная проверка для части даты "Год"
        try:
            if dict_to_validate['year'] < 1900 or dict_to_validate['year'] > 2100:
                dict_to_validate['year'] = None
        except TypeError:
            dict_to_validate['year'] = None

        return dict_to_validate


# Создать объект класса Дата
new_date = Date(f'{randint(1, 30):02}-{randint(1, 12):02}-{randint(1900, 2100)}')
print(new_date.dict_date)

# Создать объект класса Дата с заведомо некорректным годом
print()
new_date_2 = Date(f'01-01-2oo5')
print(new_date_2.dict_date)

# Создать объект класса Дата с заведомо некорректными днём и годом
print()
new_date_3 = Date(f'00-10-2200')
print(new_date_3.dict_date)
