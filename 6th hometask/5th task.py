# Определение родительского класса Канцелярская принаджность
class Stationary:
    # Получение атрибута Название из обязательного аргумента при помощи конструктора
    def __init__(self, title):
        self.title = title

    # Метод Отрисовка
    def draw(self):
        # Отобразить сообщение
        print(f'{self.title}:\tЗапуск отрисовки.')


# Определение дочернего класса Ручка
class Pen(Stationary):
    # Переопределение метода Отрисовка
    def draw(self):
        # Отобразить уникальное сообщение
        print(f'{self.title}:\tРучка не стирается ластиком.')


# Определение дочернего класса Карандаш
class Pencil(Stationary):
    # Переопределение метода Отрисовка
    def draw(self):
        # Отобразить другое уникальное сообщение
        print(f'{self.title}:\tКарандаш стирается ластиком.')


# Определение дочернего класса Маркер
class Handle(Stationary):
    # Переопределение метода Отрисовка
    def draw(self):
        # Уникально ничего не делать
        pass


new_stationary = Stationary('Something')
new_stationary.draw()

new_pen = Pen('New_pen')
new_pen.draw()

new_pencil = Pencil('New pencil')
new_pencil.draw()

new_handle = Handle('New handle')
new_handle.draw()
