def func_capitalize(f_str):
    """
    Функция принимает строку и делает каждое слово строки заглавным

    :param f_str:   строка на ввод
    :return:        возврат каже строки
    """

    def int_func(f_str):
        """
        Функция принимает строку и делает нулевой символ строки заглавным

        :param f_str:   строка на ввод
        :return:        возврат также строки
        """

        # Локальную переменную "f_str" присваиваем самой себе с методом "сделать заглавным символом"
        f_str = f_str.capitalize()

        return f_str

    # разбиваем строку на слова и помещаем в список
    f_list = f_str.split()

    # для каждого элемента списка применяем функцию озаглавливания
    f_result = list(map(int_func, f_list))

    # записываем в строку новый список с заглавными словами
    f_str = ' '.join(f_result)

    return f_str


print(func_capitalize(input(f'Enter some words: ')))
