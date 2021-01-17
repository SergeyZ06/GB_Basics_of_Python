from random import randint


# Строка для хранения имена файла
file_name = '5th task.txt'
# Счётчик для записи чисел в файл
i = 10
# Переменная для суммирвоания чисел
sum_digits = 0

# Генерация случайных чисел в списке
list_random_numbers = [randint(0, 100) for j in range(1, i + 1)]
# Запись сгенерированных чисел в строку через пробел
str_random_numbers = ' '.join(str(j) for j in list_random_numbers)

# Менеджер контекста: создание/перезапись файла для записи набора чисел
with open(file_name, 'w') as file:
    # Запись в файл строки с числами
    file.write(str_random_numbers)

# Менеджер контекста: открытие файла в режиме чтения для чтения чисел
with open(file_name, 'r') as file:
    # Для каждого обнаруженного числа в файле
    for digit in file.read().split():
        # суммировать в переменную
        sum_digits += int(digit)

print(f'Totals:\t{sum_digits}')
