print(f'Hello! Its fourth task here')

print(f'There we can try to figure out the biggest digit among others')
var_d = input(f'Please say some digits without any gaps: ')

# variable for saving max digit
var_max = 0
# variable for counting
i = 0

while i < len(var_d):
    # print(var_d[i])
    if int(var_d[i]) > var_max:
        var_max = int(var_d[i])
    i += 1

print(f'The biggest digit is: {var_max}')
