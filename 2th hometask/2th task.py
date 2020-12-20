list_a = [5, 10, True, -12.5, (1, 0), False, 'aaa', None, 10]

a = 0

while a < len(list_a):
    if a % 2 == 0 and a + 1 < len(list_a):
        list_a[a], list_a[a + 1] = list_a[a + 1], list_a[a]
    a += 1

print(list_a)
