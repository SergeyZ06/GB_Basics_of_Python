from sys import argv

script_name, hours, hour_cost, extra_pay = argv

try:
    hours = float(hours)
    hour_cost = float(hour_cost)
    extra_pay = float(extra_pay)
except ValueError:
    exit('Cannot use arguments, they should be only digits')

print(f'Wage: {hours * hour_cost + extra_pay}')
exit('Script has finished properly')
