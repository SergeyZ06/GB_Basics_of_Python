def my_func(arg1=0, arg2=0, arg3=0):
    """
    Функция принимает три позиционных аргумента и возвращает значение суммы двух наибольших аргументов

    :param arg1:    первый позиционный аргумент
    :param arg2:    второй позиционный аргумент
    :param arg3:    третий позиционный аргумент
    :return:        сумма двух наибольших аргументов
    """

    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
        arg3 = float(arg3)
    except ValueError:
        return None

    # список аргументов
    list_args = [arg1, arg2, arg3]

    # поиск первого максимального аргумента
    first_max = max(list_args)

    # удаление первого максимального элемента из списка
    list_args.remove(first_max)

    # поиск следующего максимального аргумента
    second_max = max(list_args)

    """ Ещё можно было сделать через list.sort, но не захотелось :D """

    return first_max + second_max


print(my_func(1, 2, 3))
