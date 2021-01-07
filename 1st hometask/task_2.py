print('Hello! Its a second task here')

print('This script aimed to convert seconds into hh:mm:ss time format')
var_seconds = int(input('Please say some digits, not alphabet characters! '))

var_minutes = var_seconds // 60
var_hours = var_minutes // 60

var_seconds = var_seconds % 60
var_minutes = var_minutes % 60

print(f'{var_hours:02}:{var_minutes:02}:{var_seconds:02}')
