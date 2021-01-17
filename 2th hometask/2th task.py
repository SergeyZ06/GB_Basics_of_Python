list_a = [5, 10, True, -12.5, (1, 0), False, 'aaa', None, 10]

for index, list_content in enumerate(list_a[::2]):
    if index < len(list_a) // 2:
        list_a[index * 2], list_a[index * 2 + 1] = list_a[index * 2 + 1], list_a[index * 2]

print(list_a)
