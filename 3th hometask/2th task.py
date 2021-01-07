def func_userdata(first_name, last_name, birth_year, current_city, email, phone_number):
    """
    Функция принимает данные о пользователе и выводит их одной строкой.

    :param first_name:      имя пользователя
    :param last_name:       фамилия пользователя
    :param birth_year:      год рождения пользователя
    :param current_city:    город проживания
    :param email:           адрес электронной почты
    :param phone_number:    номер телефона
    :return:
    """

    print(f'Имя: {first_name}, фамилия: {last_name}, год рождения: {birth_year}, город проживания: {current_city}, почта: {email}, тлф.: {phone_number}')


list_userdata = (f'Ivan', f'Ivanov', 1993, f'Kirov', f'IIvanov@mail.ru', f'+7(000)0000000')
func_userdata(first_name=list_userdata[0], last_name=list_userdata[1], birth_year=list_userdata[2], current_city=list_userdata[3], email=list_userdata[4], phone_number=list_userdata[5])
