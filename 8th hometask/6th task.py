from abc import abstractmethod


# Класс Исключение при некорректном вводе кода оргтехники
class ExceptionDeviceID(Exception):
    def __init__(self, message):
        self.message = message


# Класс Склад
# store_id              - код склада, целочисленный атрибут
# store_capacity        - вместимость склада, целочисленный атрибут
# store_description     - краткое описание склада, опциональный строковый атрибут
# dict_stored_devices   - словарь для хранения информации о размещении оргтехники в подразделении:
#   код оргтехники: код подразделения
class StorehouseOfficeDevice:
    # ==========
    # Попытка сделать обращения между разными классами при помощи словаря класса, а не объекта
    # Далее код попытки будет оформлен данными символами
    # ==========
    global_dict_stored_devices = {}

    def __init__(self, store_id, store_capacity, store_description=None):
        self.store_id = store_id
        self.store_capacity = store_capacity
        self.store_description = store_description
        self.dict_stored_devices = {}

    # Метод Получить оргтехнику
    # device_id - список кодов оргтехники
    def get_device(self, *device_id):
        for key in device_id:
            self.dict_stored_devices[key] = self.store_id
            StorehouseOfficeDevice.global_dict_stored_devices[key] = self.store_id

    # Метод Переместить оргтехнику
    # device_id - словарь с информацией о перемещении:
    #   код оргтехники: код подразделения
    def relocate_device(self, **device_id):
        for key in device_id.keys():
            self.dict_stored_devices[key] = device_id.get(key)
            # Здесь наверно нужно вызвать метод оргтехники Переместить оргтехнику,
            # но не понимаю как можно реализовать обращение к ещё не объявленному объекту класса Оргтехника
            # Printer.relocate_device(device_id.get(key))
            # Scanner.relocate_device(device_id.get(key))
            # Xerox.relocate_device(device_id.get(key))
            StorehouseOfficeDevice.global_dict_stored_devices[key] = device_id.get(key)


# Класс Оргтехника
# device_id - код оргтехники, целочисленный атрибут
# model     - модель, стоковый атрибут
# cost      - стоимость в долларах, числовой атрибут
# maker     - производитель, опциональный строковый атрибут
class OfficeDevice:
    def __init__(self, device_id, location, model, cost, maker=None):
        self.device_id, self.location, self.model, self.cost, self.maker = device_id, location, model, cost, maker

    # Метод Амортизация оргтехники
    @abstractmethod
    def discount(self):
        self.cost = self.cost * 0.9

    # Метод Переместить оргтехнику
    @abstractmethod
    def relocate_device(self, location):
        self.location = location
        # ==========
        # Обращение к словарю класса
        # ==========
        StorehouseOfficeDevice.global_dict_stored_devices[self.device_id] = location


# Класс Принтер
# Наследует все атрибуты класса Ортехника
# color - цвет печати, строковый атрибут
class Printer(OfficeDevice):
    def __init__(self, device_id, location, model, cost, color, maker=None):
        # Проверка ввода кода оргтехники
        try:
            # Если переданный параметр целочисленный
            if device_id.isdigit():
                # записать значение параметра в атрибут оргтехники
                self.color = color
                super(Printer, self).__init__(device_id, location, model, cost, maker)
            # иначе
            else:
                # поднять исключение
                raise ExceptionDeviceID(f'Device ID "{device_id}" specified incorrect.')
        # Перехватить исключение
        except ExceptionDeviceID as error:
            # вывести сообщение об ошибке
            print(error.message)

    # Метод Амортизация оргтехники
    def discount(self):
        self.cost = self.cost * 0.9

    # Метод Переместить оргтехнику
    def relocate_device(self, location):
        self.location = location
        # ==========
        # Обращение к словарю класса
        # ==========
        StorehouseOfficeDevice.global_dict_stored_devices[self.device_id] = location


# Класс Сканер
# Наследует все атрибуты класса Ортехника
# size  - диагональ сканера в дюймах, числовой атрибут
class Scanner(OfficeDevice):
    def __init__(self, device_id, location, model, cost, size, maker=None):
        # Проверка ввода кода оргтехники
        try:
            # Если переданный параметр целочисленный
            if device_id.isdigit():
                # записать значение параметра в атрибут оргтехники
                self.size = size
                super(Scanner, self).__init__(device_id, location, model, cost, maker)
            # иначе
            else:
                # поднять исключение
                raise ExceptionDeviceID(f'Device ID "{device_id}" specified incorrect.')
        # Перехватить исключение
        except ExceptionDeviceID as error:
            # вывести сообщение об ошибке
            print(error.message)

    # Метод Амортизация оргтехники
    def discount(self):
        self.cost = self.cost * 0.9

    # Метод Переместить оргтехнику
    def relocate_device(self, location):
        self.location = location
        # ==========
        # Обращение к словарю класса
        # ==========
        StorehouseOfficeDevice.global_dict_stored_devices[self.device_id] = location


# Класс Ксерокс
# Наследует все атрибуты класса Ортехника
# paper_format  - типы используемой бумаги, список строк
class Xerox(OfficeDevice):
    def __init__(self, device_id, location, model, cost, *paper_format, maker=None):
        # Проверка ввода кода оргтехники
        try:
            # Если переданный параметр целочисленный
            if device_id.isdigit():
                # записать значение параметра в атрибут оргтехники
                self.paper_format = paper_format
                super(Xerox, self).__init__(device_id, location, model, cost, maker)
            # иначе
            else:
                # поднять исключение
                raise ExceptionDeviceID(f'Device ID "{device_id}" specified incorrect.')
        # Перехватить исключение
        except ExceptionDeviceID as error:
            # вывести сообщение об ошибке
            print(error.message)

    # Метод Амортизация оргтехники
    def discount(self):
        self.cost = self.cost * 0.9

    # Метод Переместить оргтехнику
    def relocate_device(self, location):
        self.location = location
        # ==========
        # Обращение к словарю класса
        # ==========
        StorehouseOfficeDevice.global_dict_stored_devices[self.device_id] = location


# Класс Подразделение
# division_id           - код подразделения, целочисленный атрибут
# division_description  - краткое описание подразделения, опциональный строковый атрибут
class Division:
    def __init__(self, division_id, division_description=None):
        self.division_id, self.division_description = division_id, division_description
        self.list_devices_in_use = []

    # Метод Получить оргтехнику
    def get_device(self, device_id):
        self.list_devices_in_use.append(device_id)
        # ==========
        # Обращение к словарю класса
        # ==========
        StorehouseOfficeDevice.global_dict_stored_devices[device_id] = self.division_id


pass
