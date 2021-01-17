from random import randint
from collections import Counter

# Создание исходного списка с использованием генератора
list_1 = list(randint(0, 21) for i in range(0, 16))
print(list_1)

# Словарь элементов и их вхождений в список list_1:
# ключ              - элемент
# значение ключа    - кол-во вхождений элемента в список
dict_counter = Counter(list_1)

# Словарь элементов для удаления
# ключ              - элемент
# значение ключа    - кол-во вхождений большее 1
dict_counter_delete = {key: dict_counter.get(key) for key in dict_counter.keys() if dict_counter.get(key) > 1}

# Для каждого элемента для удаления
for key in dict_counter_delete.keys():
    # обнулить счётчик колличества удалений элемента
    i = 0
    # пока элемент не будет удалён столько раз, сколько он присутствует в списке
    while i < dict_counter_delete.get(key):
        # инкрементировать счётчик
        i += 1
        # удалять элемент из списка
        list_1.remove(key)

print(list_1)
