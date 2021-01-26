# Класс Склад
# store_id          - номер склада, целочисленный атрибут
# store_capacity    - вместимость склада, целочисленный атрибут
# store_description - краткое описание склада, опциональный строковый атрибут
class StorehouseOfficeDevice:
    def __init__(self, store_id, store_capacity, store_description=None):
        self.store_id = store_id
        self.store_capacity = store_capacity
        self.store_description = store_description


# Класс Оргтехника
# model - модель, стоковый атрибут
# cost  - стоимость в долларах, числовой атрибут
# maker - производитель, опциональный строковый атрибут
class OfficeDevice:
    def __init__(self, model, cost, maker=None):
        self.model, self.cost, self.maker = model, cost, maker


# Класс Принтер
# Наследует все атрибуты класса Ортехника
# color - цвет печати, строковый атрибут
class Printer(OfficeDevice):
    def __init__(self, model, cost, color, maker=None):
        self.color = color
        super(Printer, self).__init__(model, cost, maker)


# Класс Сканер
# Наследует все атрибуты класса Ортехника
# size  - диагональ сканера в дюймах, числовой атрибут
class Scanner(OfficeDevice):
    def __init__(self, model, cost, size, maker=None):
        self.size = size
        super(Scanner, self).__init__(model, cost, maker)


# Класс Ксерокс
# Наследует все атрибуты класса Ортехника
# paper_format  - типы используемой бумаги, список строк
class Xerox(OfficeDevice):
    def __init__(self, model, cost, *paper_format, maker=None):
        self.paper_format = paper_format
        super(Xerox, self).__init__(model, cost, maker)


pass
