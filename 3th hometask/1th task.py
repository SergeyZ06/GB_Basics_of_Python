
def func_div(arg1, arg2):
    """
    Функция деления первого аргумента на второй

    arg1    - первый аргумент, делимое, должен быть int или float
    arg2    - второй аргумент, делитель, должен быть int или float
    res     - результат деления, функция возвращает его значение

    Пример вызова:
    print(func_div(3, 2))
    >>> 1.5

    Если значения аргументов указаны некорректно:
        - тип аргументов отличен от int или float;
        - второй аргумент, делитель, равен нулю,
    функция вернёт значение None
    """

    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
    except ValueError:
        return None

    try:
        res = arg1 / arg2
    except ZeroDivisionError:
        return None

    return res


print(f'Result is: ', func_div(input(f'Enter number you wanna divide: '), input(f'Enter number you wanna divine on: ')))
