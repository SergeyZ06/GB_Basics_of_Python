# Строка для хранения имени исходного файла
file_name_old = '4th task.txt'
# Строка для хранения имени нового файла
file_name_new = '4th task new.txt'
# Словарь для замены английских слов на русские
dict_digits = {
    'One':      'Один',
    'Two':      'Два',
    'Three':    'Три',
    'Four':     'Четыре'
}

# Менеджер контекста: открытие старого файла в режиме чтения,
# создание/перезапись нового файла в режиме записи
with open(file_name_old, 'r') as file_old, open(file_name_new, 'w') as file_new:
    # Для каждой строки в старом файле
    for lines_old in file_old:
        # для каждого ключа словаря
        for dict_keys in dict_digits.keys():
            # искать наличие ключей словаря в каждой строке старого файла
            if lines_old.find(dict_keys) != -1:
                # если ключ найдет, то отредактировать строку:
                # заменить в строке найденный ключ на значение ключа
                lines_old = lines_old.replace(dict_keys, dict_digits.get(dict_keys), 1)
        # Запись отредактированной строки в новый файл
        file_new.write(lines_old)

# Проверка записи нового файла
with open(file_name_new, 'r') as file_new:
    print(file_new.read())
