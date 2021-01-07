month = int(input(f'Select number of month from 1 to 12 please: '))

# Solution with lists
list_month = (
    'Its a winter!',
    'Its a winter!',
    'Its a spring!',
    'Its a spring!',
    'Its a spring!',
    'Its a summer!',
    'Its a summer!',
    'Its a summer!',
    'Its a fall!',
    'Its a fall!',
    'Its a fall!',
    'Its a winter!'
)

print(list_month[month - 1])

# Solution with a dictionary
dict_month = {
    12: 'Its a winter!',
    1:  'Its a winter!',
    2:  'Its a winter!',
    3:  'Its a spring!',
    4:  'Its a spring!',
    5:  'Its a spring!',
    6:  'Its a summer!',
    7:  'Its a summer!',
    8:  'Its a summer!',
    9:  'Its a fall!',
    10: 'Its a fall!',
    11: 'Its a fall!'
}

print(dict_month.get(month))
