from functools import reduce


# Функция вычисления произведения двух аргументов
def func_multiply(arg1=1, arg2=1):
    return arg1 * arg2


# Генерация списка элементов от 100 до 1000 с шагом 2
list_1 = list(i for i in range(100, 1002, 2))
print(list_1)

# Вычисление произведения всех элементов списка list_1
result = reduce(func_multiply, list_1)
print(result)
