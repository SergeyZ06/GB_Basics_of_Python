from random import randint


def func_delete(list_d):
    """
    Функция проверяет соседние элементы
    Если следующий элемент меньше предыдущего, то следующий удаляется

    :param list_d:  Список на ввод
    :return:        Список на вывод
    """

    # Формирования нового списка
    list_check = list()

    # Первый элемент не подлежит проверке, переносится в новый список и старого
    list_check.append(list_d[0])

    # Для каждого элемента старого списка
    # index - номер элемента в редактируемом списке
    # value     - значение элемента
    for index, value in enumerate(list_d):
        # Начиная со второго элемента
        if index > 0:
            # Проверить, больше ли он предыдущего элемента
            if list_d[index] > list_d[index - 1]:
                # Если больше, то записать текущий элемент в новй список
                list_check.append(value)

    # Возврат сформированного списка
    return list_check


# Генерация исходного списка, десять элементов-чисел со значениями от 0 до 299
list_1 = list(randint(0, 300) for i in range(1, 10))
print(list_1)

# Обновление исодного списка с использованием функции
# list_1 = func_delete(list_1)
print(func_delete(list_1))

print(list(value for index, value in enumerate(list_1) if index == 0 or (index > 0 and value > list_1[index - 1])))
