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
        # Получение фамилии сотрудника и зарплаты из строки файла
        line_person, line_wage = line.split()
        # Суммирование всех зарплат
        avg_wage += int(line_wage)
        # Подсчёт колличества сотрудников
        employee_count += 1
        # Анализ зарплаты
        if float(line_wage) < 20000:
            print(f'{line_person} has wage less than 20000')

    # Вычисление средней заработной платы
    avg_wage = avg_wage / employee_count
    print(f'Average wage is {avg_wage}')
