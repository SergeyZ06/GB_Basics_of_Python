import time


# Определение класса Светофор
class TrafficLight:
    # Приватный словарь для хранения соответствий цвета сигнала и времени оторажения сигнала
    # 'Цвет сигнала': время отображения
    __dict_colors = {'red': 7, 'yellow': 2, 'green': 5}

    # Метод Запуск светофора
    def running(self):
        # Защищённая переменная для отображения текущего сигнала светофора
        self._color = None

        # Для всех ключей в словаре
        for self._color in TrafficLight.__dict_colors.keys():
            # отобразить текущий сигнал и время отображения
            print(f'{self._color}\t\t - wait {TrafficLight.__dict_colors.get(self._color)} second(s)')
            # ждать кол-во секунд равное значению ключа в словаре
            time.sleep(TrafficLight.__dict_colors.get(self._color))


# Создание объекта класса Светофор
new_trafficlight = TrafficLight()
# Запуск метода Запуск светофора
new_trafficlight.running()
