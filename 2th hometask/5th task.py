list_a = [2, 5, 6, 8, 3]

list_a.sort(reverse=True)

print(f'We have a rating: {list_a}')

a = input(f'Add some new integer to the rating: ')

list_a.append(int(a))

list_a.sort(reverse=True)

print(f'New rating is: {list_a}')
