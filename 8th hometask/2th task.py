# Исключение для обработки деления на нуль
class MyZeroDivision(Exception):
    def __init__(self, strange_message):
        self.strange_message = strange_message


# Исключение для обработки преобразования строки в число
class MyValueError(Exception):
    def __init__(self, another_strange_message):
        self.another_strange_message = another_strange_message


# Запрос переменных для деления у пользователя
# var_a - переменная для делимого
# var_b - переменная для делителя
var_a = input(f'Enter some digit to divide it: ')
var_b = input(f'Enter some digit to divide first digit on it: ')

# Попробовать преобразовать значение переменной var_a
try:
    # Если значение переменной является числом
    if var_a.isdigit():
        # преобразовать переменную
        var_a = float(var_a)
    # иначе
    else:
        # поднять исключение
        raise MyValueError(f'Var_a has not a numeric value')
# Перехватить исключение
except MyValueError as my_value_error_var_a:
    # Вывести очень важное сообщение
    print(my_value_error_var_a.another_strange_message)
    # Завершить программу с аварийным кодом
    exit(1)
# Иначе
else:
    # Вывести сообщение, что всё хорошо
    print(f'Value of var_a successfully became numeric: {var_a}')

# Аналогичный алгоритм для преобзования переменной var_b
try:
    if var_b.isdigit():
        var_b = float(var_b)
    else:
        raise MyValueError(f'Var_b has not a numeric value')
except MyValueError as my_value_error_var_b:
    print(my_value_error_var_b.another_strange_message)
    exit(1)
else:
    print(f'Value of var_b successfully became numeric: {var_b}')

# Попробовать выполнить деление
try:
    # Если значение делителя равно нулю
    if var_b == 0:
        # поднять исключение
        raise MyZeroDivision(f'Oops, something went wrong! Are you sure you have not tried to divide on zero?')
    # иначе
    else:
        # выполнить деление и сохранить результат в новую переменную
        var_division_result = var_a / var_b
# Перехватить исключение
except MyZeroDivision as my_zero_division_result:
    # Вывести ещё более важное сообщение
    print(my_zero_division_result.strange_message)
    # Завершить программу с аварийным кодом
    exit(1)
# Иначе
else:
    # Вывести сообщение с результатом деления
    print(f'Here is the result: {var_division_result}')
# в конце
finally:
    # Вывести сообщение, что программа звершила работу штатно
    print(f'Program has finished properly')
