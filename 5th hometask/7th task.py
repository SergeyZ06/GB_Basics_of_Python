import json


# Строка для хранения названия файла
file_name = '7th task.txt'
# Переменная для хранения кол-ва прибыльных фирм
count_profit = 0
# Переменная для вычисления средней прибыли
avg_profit = 0

# Менеджер контекста: открытие файла в режиме чтения
with open(file_name, 'r') as file:
    # Для каждой строки файла
    for file_lines in file:
        # получить список слов в строке
        file_list = file_lines.split()
        # вычислить прибыль для каждой фирмы
        print(f'{file_list[0]} profit is:\t{int(file_list[2]) - int(file_list[3])}')
        # Если прибыль фирмы больше/равна нулю
        if int(file_list[2]) - int(file_list[3]) >= 0:
            # учесть фирму среди прибыльных, записать прибыль
            count_profit += 1
            avg_profit = avg_profit + int(file_list[2]) - int(file_list[3])
    print(f'Average profit is:\t{avg_profit / count_profit}')

print(f'')
print(f'===========================================================================')
print(f'')

# Список из двух словарей:
# словарь 1:    ключ - название фирмы, значение ключа - прибыль фирмы
# словарь 2:    ключ - строка "средняя прибыль", значение ключа - вычисленная средняя прибыль
list_dict_firms = [{}, {}]

# Менеджер контента: открытие файла в режиме чтения
with open(file_name, 'r') as file:
    # Для каждой строки файла
    for file_lines in file:
        # получить список слов в строке
        file_list = file_lines.split()
        # записать в первый словарь название фирмы и значение прибыли
        list_dict_firms[0][file_list[0]] = int(file_list[2]) - int(file_list[3])

# Определение первого элемента второго словаря
list_dict_firms[1]['average_profit'] = 0

# Для каждого значения прибыли в первом словаре
for i in list_dict_firms[0].values():
    # суммировать прибыль в значение втого словаря
    list_dict_firms[1]['average_profit'] = list_dict_firms[1].get('average_profit') + i

# Во втором словаре
# разделить суммарную прибыль на кол-во фирм из первого словаря
list_dict_firms[1]['average_profit'] = list_dict_firms[1].get('average_profit') / len(list_dict_firms[0].values())

print(list_dict_firms)

print(f'')
print(f'===========================================================================')
print(f'')

# Строка для ранения имени json-файла
file_json_name = '7th task.json'

# Менеджер контекста: создание/перезапись файла в режиме записи
with open(file_json_name, 'w') as file:
    # Запись object словарь list_dict_firms в файл
    json.dump(list_dict_firms, file)

# Менеджер контекста: открытие файла в режиме чтения
with open(file_json_name, 'r') as file:
    # Проверка записи json-файла
    print(file.read())
