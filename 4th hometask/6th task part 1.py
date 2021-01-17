from sys import argv
from itertools import count


script_name, var_iter = argv

# Попробовать получить число из параметра
try:
    var_iter = int(var_iter)
# Если не получается, то заругаться
except ValueError:
    exit('Cannot use argument, it should be only digits')

# Определить границы итерации, 10 раз
var_iter_finish = var_iter + 10

# Итерировать пока границы итерации не достигнуты
for i in count(var_iter):
    if i > var_iter_finish:
        break
    print(i)

exit('Script has finished properly')
