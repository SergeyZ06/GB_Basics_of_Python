print('Hello! Its a second task here')

print('This script aimed to convert seconds into hh:mm:ss time format')
var_seconds = int(input('Please say some digits, not alphabet characters! '))

print(f'Lets try to calculate: {var_seconds // 3600}:{(var_seconds - (var_seconds // 3600) * 3600) // 60}:{var_seconds % 60}')