list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_fall = [9, 10, 11]

month = int(input(f'Select number of month from 1 to 12 please: '))

# Solution with lists
for b in list_winter:
    if month == b:
        print(f'Its a winter!')

for b in list_spring:
    if month == b:
        print(f'Its a spring!')

for b in list_summer:
    if month == b:
        print(f'Its a summer!')

for b in list_fall:
    if month == b:
        print(f'Its a fall!')

# Solution with dictionary
dict_m = dict(list_winter=[12, 1, 2], list_spring=[3, 4, 5], list_summer=[6, 7, 8], list_fall=[9, 10, 11])

for b in dict_m:
    for c in dict_m.get(b):
        if month == c:
            if b == 'list_winter':
                print(f'Its a winter!')
            elif b == 'list_spring':
                print(f'Its a spring!')
            elif b == 'list_summer':
                print(f'Its a summer!')
            elif b == 'list_fall':
                print(f'Its a fall!')
