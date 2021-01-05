# Строка для хранения имени файла
file_name = '3th task.txt'
# Переменная для вычисления средней заработной платы
avg_wage = 0
# Переменная для подсчёта колличества сотрудников
employee_count = 0

# Открытие файла при помощи менеджера контекста
with open(file_name, 'r') as file:

    # Построчное чтение файла
    for line in file:
        # Суммирование всех зарплат
        avg_wage = avg_wage + int(line.split()[1])
        # Подсчёт колличества сотрудников
        employee_count += 1
        # Поиск и анализ втрого слова в кажой строке - зарплаты
        if float(line.split()[1]) < 20000:
            print(f'{line.split()[0]} has wage less than 20000')

    # Вычисление средней заработной платы
    avg_wage = avg_wage / employee_count
    print(f'Average wage is {avg_wage}')
