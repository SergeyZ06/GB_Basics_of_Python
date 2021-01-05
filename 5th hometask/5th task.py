from random import randint


# Строка для хранения имена файла
file_name = '5th task.txt'
# Счётчик для записи чисел в файл
i = 10
# Переменная для суммирвоания чисел
sum_digits = 0

# Менеджер контекста: создание/перезапись файла для записи набора чисел
with open(file_name, 'w') as file:
    # Запись первого числа в файл
    file.write(str(randint(0, 100)))
    # Цикл для записи чисел через пробел
    while i > 0:
        i -= 1
        file.writelines(' ' + str(randint(0, 100)))

# Менеджер контекста: открытие файла в режиме чтения для чтения чисел
with open(file_name, 'r') as file:
    # Для каждого обнаруженного числа в файле
    for digit in file.read().split():
        # суммировать в переменную
        sum_digits = sum_digits + int(digit)

print(f'Totals:\t{sum_digits}')
