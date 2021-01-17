# Финальный список со всеми моделями
list_models = []

# Кортеж, содержащий информацию о товаре
list_models_tuple = ()

# Список для формирования кортежа
list_models_tuple_list = []

# Номер товара в списке, указывается в кортеже
list_models_tuple_id = 0

# Словарь, содержащий информацию о товаре, хранится в кортеже
list_models_tuple_dict = dict(name=None, price=None, count=None, measurement=None)

# Словарь для аналитики товаров
dict_models = dict(name=None, price=None, count=None, measurement=None)

# Список для заполнения аналитического словаря
dict_models_list = []

while 1 == 1:
    print('Do you wanna add yet another model to list?')
    var_ask = input(f'Type "yes" or "no": ')

    if var_ask == 'no':
        print(f'Adding mode is over')
        break

    list_models_tuple_id += 1
    list_models_tuple_dict['name'] = input(f'Enter name of product: ')
    list_models_tuple_dict['price'] = input(f'Enter price of product: ')
    list_models_tuple_dict['count'] = input(f'Enter count of product: ')
    list_models_tuple_dict['measurement'] = input(f'Enter measurement of product: ')
    # Следующая строка кода помещает во временный список id записи и словарь
    list_models_tuple_list = (list_models_tuple_id, list_models_tuple_dict)
    # Следующая строка кода формирует кортеж
    list_models_tuple = list_models_tuple_list
    # Добавляем главному списку новый элемент - сформированный кортеж
    list_models.append(tuple(list_models_tuple))
    # Очищаем временный словарь для записи следующих продуктов
    list_models_tuple_dict = dict(name=None, price=None, count=None, measurement=None)

if not list_models:
    print(f'Models list is empty')
else:
    print(f'Models list is formed:')
    for i in list_models:
        print(i)

# Вытаскиваем из главного списка все имена
    for index, var in enumerate(list_models):
        # Для каждого элемента главного списка - кортежа который там хранится, копируем значение в другой список
        list_models_tuple_list = list_models[index]
        for index2, var2 in enumerate(list_models_tuple_list):
            # Для каждого скопированного кортежа работаем только с его вторым элементом - словарём
            # Первый элемент не нужен, так как там находится id записи
            if index2 == 1:
                # Из словаря извлекаем значение поля "имя" и прибавляем к другому временному списку
                dict_models_list.append(var2['name'])
# Помещаем имена из другого временного списка в аналитический словарь
    dict_models['name'] = list(dict_models_list)
# Очищаем список, чтобы использовать его далее для получения списков цен, колличества и единиц измерения
    dict_models_list.clear()

# Далее по аналогии для цен
    for index, var in enumerate(list_models):
        list_models_tuple_list = list_models[index]
        for index2, var2 in enumerate(list_models_tuple_list):
            if index2 == 1:
                dict_models_list.append(var2['price'])
    dict_models['price'] = list(dict_models_list)
    dict_models_list.clear()

# Далее по аналогии для колличества товара
    for index, var in enumerate(list_models):
        list_models_tuple_list = list_models[index]
        for index2, var2 in enumerate(list_models_tuple_list):
            if index2 == 1:
                dict_models_list.append(var2['count'])
    dict_models['count'] = list(dict_models_list)
    dict_models_list.clear()

# Далее по аналогии для единиц измерения товара
    for index, var in enumerate(list_models):
        list_models_tuple_list = list_models[index]
        for index2, var2 in enumerate(list_models_tuple_list):
            if index2 == 1:
                dict_models_list.append(var2['measurement'])
    dict_models['measurement'] = list(dict_models_list)

    print(f'Analytical dictionary is formed: ')
    for i in dict_models:
        print(f'{i}: {dict_models[i]}')
