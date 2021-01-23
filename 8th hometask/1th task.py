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
        self.str_date = str_data

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
    def date_validation(str_to_validate):
        # Преобразовать строковую запись даты в словарь с частями даты
        dict_to_validate = Date.date_to_numeric(str_to_validate)

        # Пробовать
        try:
            # оценить часть даты "День"
            if dict_to_validate['day'] < 1 or dict_to_validate['day'] > 31:
                # в случае некорректного значения вывести сообщение
                print(f'Part "day" of {str_to_validate} is not correct')
        # в случае невозможности сравнения
        except TypeError:
            # вывести сообщение
            print(f'Part "day" of {str_to_validate} is not correct')

        # Аналогичная проверка для части даты "Месяц"
        try:
            if dict_to_validate['month'] < 1 or dict_to_validate['month'] > 12:
                print(f'Part "month" of {str_to_validate} is not correct')
        except TypeError:
            print(f'Part "month" of {str_to_validate} is not correct')

        # Аналогичная проверка для части даты "Год"
        try:
            if dict_to_validate['year'] < 1900 or dict_to_validate['year'] > 2100:
                print(f'Part "year" of {str_to_validate} is not correct')
        except TypeError:
            print(f'Part "year" of "{str_to_validate}" is not correct')


# Создать объект класса Дата
new_date = Date(f'{randint(1, 30):02}-{randint(1, 12):02}-{randint(1900, 2100)}')
# Отобразить содержимое объекта
print(new_date.str_date)
# Отобразить результат рабты метода Преобразования
print(Date.date_to_numeric(new_date.str_date))
# Вызвать метод Проверки даты
Date.date_validation(new_date.str_date)

# Создать объект класса Дата с заведомо некорректным годом
print()
new_date_2 = Date(f'01-01-2oo5')
print(Date.date_to_numeric(new_date_2.str_date))
Date.date_validation(new_date_2.str_date)

# Создать объект класса Дата с заведомо некорректными днём и годом
print()
new_date_3 = Date(f'00-10-2200')
print(Date.date_to_numeric(new_date_3.str_date))
Date.date_validation(new_date_3.str_date)
