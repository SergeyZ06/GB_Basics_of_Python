print(f'Hello! Fifth task there')

print('During this task we will try to calculate profit or deficit of some firm')
var_i = float(input(f'Please tell me income: '))
var_e = float(input(f'Please tell me expenses: '))

print(f'Income: {var_i}')
print(f'Expenses: {var_e}')

if var_i > var_e:
    print(f'The firm has a profit: {var_i - var_e}')
    var_staff = int(input(f'Lets split the profit on whole staff. How many employees are there? '))
    print(f'Benefit on one employee is: {(var_i - var_e) / var_staff}')

elif var_i == var_e:
    print(f'The firm doesnt have profit as well as losses')

elif var_i < var_e:
    print(f'The firm has losses: {abs(var_i - var_e)}')