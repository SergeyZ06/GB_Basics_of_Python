from functools import reduce


# Функция-генератор факториалов
def func_gen(arg_1):
    # Функция вычисления произведения двух аргументов
    def func_multiply(func_multiply_arg_1, func_multiply_arg_2):
        return func_multiply_arg_1 * func_multiply_arg_2

    # Счётчик для последовательного вычисления факториалов
    i = 0

    # Для каждого числа от 1 до числа переданного в функцию
    while i < arg_1:
        i += 1
        # вычислить факториал
        # вернуть вычисленный факториал как очередное значение счётчика
        yield reduce(func_multiply, list(j for j in range(1, i + 1)))


var_iter = int(input(f'Enter some digit for calculating factorials from 1 to this digit: '))

print(f'Its a generator: {func_gen(var_iter)}')

for index, value in enumerate(func_gen(var_iter)):
    print(f'Factorial of {index + 1} is: {value}')
