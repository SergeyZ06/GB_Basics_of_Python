# Исключение для ловли символов, претворяющихся числами
class MyStrangeException(Exception):
    def __init__(self, strange_message):
        self.strange_message = strange_message


# Список для хранения чисел, вводимых пользователем
list_digits = []
# Переменная для промежуточного хранения вводимого символа
var_input = 0

print(f'Hello there!')
print(f'You can type some digits one by one with pressing Enter')
print(f'Note: we will check them all!')

# Цикл выполняется до обнаружения стоп-слова
while True:
    # Запрос символа у пользователя
    var_input = input(f'Type digit please. If you wanna stop, type "stop": ')

    # Если пользователь ввёл стоп-слово
    if var_input == 'stop':
        # вывывести сообщение, что стоп-слово обнаружено, что будет выведен список введённых чисел
        print(f'"stop" has been detected, lets look list of digits:')
        # вывести список введённых чисел
        print(list_digits)
        # прервать цикл
        break

    # Пробовать
    try:
        # проверить, если символ является числом
        if var_input.isdigit():
            # добавить в список новый элемент - символ, преобразованный в число
            list_digits.append(int(var_input))
        # если символ оказался не числом
        else:
            # поднять исключение для ловли символов-нарушителей
            raise MyStrangeException(f'"{var_input}" does not look like digit, be careful next time!')
    # перехватить исключение
    except MyStrangeException as new_exception:
        # вывести очень важное сообщение
        print(new_exception.strange_message)
