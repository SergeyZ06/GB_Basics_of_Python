from random import randint

# Создание исходного списка с использованием генератора
list_1 = list(randint(0, 21) for i in range(0, 16))
print(list_1)

# Созданире списка, для хранения уникальных элементов из списка list_1
list_2 = list()

# Для каждого элемента списка list_1
for i in list_1:
    # Если кол-во вхождений элемента в список list_1 равно одному
    if list_1.count(i) == 1:
        # Записать уникальный элемент в список list_2
        list_2.append(i)

print(list_2)
