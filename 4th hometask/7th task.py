from functools import reduce


# Функция-генератор факториалов
def func_gen(arg_1):
    # Функция вычисления произведения двух аргументов
    def func_multiply(func_multiply_arg_1, func_multiply_arg_2):
        return func_multiply_arg_1 * func_multiply_arg_2

    # Список элементов от 1 до заданного числа, для которых необходимо вычислить фактоиалы
    list_1 = list(i1 for i1 in range(1, arg_1 + 1))
    # Пустой список, в котором будут храниться вычисленные факториалы
    list_2 = list()
    # Пустой список, в котором будут храниться промежуточные вычисления фактриалов
    list_3 = list()

    # Для каждого элемента в списке list_1 - список чисел от 1 до заданного числа с шагом 1
    for i2 in list_1:
        # Добавить в список list_3 элемент списка list_1, для промежуточного вычисления факториала
        # от 1 до текущего элемента
        list_3.append(i2)
        # Добавить в список list_2 вычисленный факториал, произведение всех элементов списка list_3
        # от 1 до текущего элемента
        list_2.append(reduce(func_multiply, list_3))

    # Возврат итерируемого элемента генератора
    # Все вычисленные факториалы хранятся в списке list_2
    for i3 in list_2:
        yield i3


var_iter = int(input(f'Enter some digit for calculating factorials from 1 to this digit: '))

print(f'Its a generator: {func_gen(var_iter)}')

for index, i in enumerate(func_gen(var_iter)):
    print(f'Factorial of {index + 1} is: {i}')
