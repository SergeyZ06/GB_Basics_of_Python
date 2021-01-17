# Строка  для хранения имени файла
file_name = '2th task.txt'
# Список для хранения содержимого файла
file_content = []
# Словарь для хранения колличества слов в строках
file_words = {}

# Чтение файла в список при помощи мнеджера контекста
with open(file_name, 'r') as file:
    file_content = file.readlines()

# Для каждого элемента списка
for index, content in enumerate(file_content):
    # записать в словарь ключ (номер элемента + 1) и колличество слов в этом элементе
    file_words[index + 1] = len(content.split())

print(f'Total number of strings: {len(file_content)}')
# Для каждой записи словаря
for index in file_words.keys():
    # отобразить ключ и значение
    print(f'String number {index} contains {file_words.get(index)} word(s)')
