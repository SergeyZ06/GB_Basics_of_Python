str_a = input(f'Enter something please: ')

# s — начало среза, f — окончание
s = 0
f = 0

# spaces - количество пробелов в строке, space - счётчик пробелов
spaces = str_a.count(' ')
space = 0

# Словарь для сохранения найденных слов
dict_str = dict()

for index, var in enumerate(str_a):
    if var == ' ':
        space += 1
        f = index
        dict_str[space] = str_a[s:f:1]
        s = index + 1
        if space == spaces:
            dict_str[space + 1] = str_a[s::1]

for i in dict_str:
    print(dict_str[i][:10])
