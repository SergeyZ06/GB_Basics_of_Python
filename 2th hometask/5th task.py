# Список с исходным рейтингом
list_a = [7, 5, 3, 3, 2]

print(f'We have a rating:\t{list_a}')

# Переменная для хранения нового элемента рейтинга
var_a = int(input(f'Add some new integer to the rating: '))

# Итератор списка с рейтингом
iterator = iter(list_a)
# Переменная для хранения значения итератора
iterator_value = 0

# Выполнять цикл пока не будет найден элемент списка меньший, чем новый элемент
# или пока не закончатся элементы списка при переборе списка
while True:
    # Пробовать
    try:
        # Получить значение очередного элемента
        iterator_value = int(next(iterator))
        # Если очередной элемент меньше нового элемента
        if var_a > iterator_value:
            # записать новый элемент на позицию текущего
            list_a.insert(list_a.index(iterator_value), var_a)
            # прервать цикл
            break
    # Если все элементы перебраны
    except StopIteration:
        # записать новый элемент в конец списка
        list_a.append(var_a)
        # прервать цикл
        break

print(f'New rating is:\t\t{list_a}')
