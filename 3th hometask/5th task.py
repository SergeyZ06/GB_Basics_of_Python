def func_digits(f_string_digits):
    """
    Функция ищет числа в строке и вычисляет их сумму

    :param f_string_digits: строка с числами
    :return:                результат суммирования найденных чисел
    """
    # разбиваем строку на слова и складываем в список
    f_list_digits = f_string_digits.split()

    # здесь будем вычислять сумму всех найденных чисел
    f_sum = 0

    # для каждого найденного слова делаем следующее:
    for digit in f_list_digits:
        # каждое слово проверяем на наличие спец-символа остановки
        # если спец-символ найден, то последующие слова не анализируем
        if digit.find('%') != -1:
            break
        # если спец-символ не найден, пытаемся преобразовать слово в число и суммируем
        try:
            f_sum += float(digit)
        # если слово не является числом, то жестоко избавляемся от него
        except ValueError:
            f_list_digits.remove(digit)

    # убиваем строку и список, чтобы они были чистыми к следующему вызову функции
    del f_string_digits
    del f_list_digits

    return f_sum


print(f'Hello there!')
print(f'You can type some digits separated with spaces and it will be summed together')
print(f'If wanna stop this type %')

#
summa = 0

# циклически спрашиваем строку
while True:
    str_digits = input(f'Type some digits: ')
    # передаём строку в функцию и суммируем полученное
    summa = summa + func_digits(str_digits)
    print(f'Here the result: {summa}')
    # если находим спец-символ, то прекращаем баловство
    if str_digits.find('%') != -1:
        break
