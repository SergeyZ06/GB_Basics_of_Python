print(f'Hello! Sixth task there')

print(f'Now we gotta calculate the day when sportsman will achieve result')
var_a = float(input(f'Please say the  distance (km): '))
var_b = float(input(f'And now please say required distance (km): '))

var_day = int(1)

while var_a < var_b:
    var_a = var_a * 1.1
    var_day += 1

print(f'The sportsman will achieve required result {var_b} km on {var_day}th day')