# Строка для хранения полученной от пользователя информации
str_in = ''
# Строка для хранения имени создаваемого файла
file_name = '1th task.txt'

print(f'Print % to stop process')

# Перезапись/создание файла при помощи менеджера контекста
with open(file_name, 'w') as file:
    # Циклический запрос данных от пользователя
    while True:
        str_in = input(f'Say something:\t')
        # Прерывание цикла при обнаружении стоп-символа
        if str_in.count('%') != 0:
            break
        # Запись данных пользователя в файл и перевод строки
        file.writelines([str_in, '\n'])

# Проверка записанной информации
with open(file_name, 'r') as file:
    print(file.read())
