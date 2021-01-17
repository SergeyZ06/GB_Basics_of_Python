def my_func(x, y):
    """
    Функция возведения числа x в степень y

    :param x:   вещественное положительное число, которое возводим в степнь
    :param y:   степень, в которую возводим, отрицательное целое число
    :return:    результат возведения числа x в степень y
    """

    # проверка корректности полученных данных
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return None

    # для удобства пользователя функция скорректирует знаки чисел
    if x < 0:
        x = -x

    if y > 0:
        y = -y

    # стандартные методы для слабаков
    # return x ** y
    # return pow(x, y)

    # здесь живёт результат вычисления
    res = 1

    # не цикл, но тоже работает
    # for i in range(0, y, -1):
    #     res = res / x

    while y < 0:
        y += 1
        res = res / x

    return res


print(my_func(input(f'Enter x: '), input(f'Enter y: ')))
