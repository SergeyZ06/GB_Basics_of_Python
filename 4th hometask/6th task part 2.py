from sys import argv
from itertools import cycle
from random import random


# Генерация действительного числа от 1 до 3
string = str(random() * 2 + 1)

script_name, count = argv

try:
    count = int(count)
except ValueError:
    exit('Cannot use argument, it should be only digits')

# Посимвольный вывод сгенерированного числа в цикле
for i in cycle(string):
    if count == 0:
        break

    print(i)
    count -= 1

exit('Script has finished properly')
