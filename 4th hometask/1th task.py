from sys import argv


def func_wage(hours=0, hour_cost=0, extra_pay=0):
    """
    Функция расчета заработной платы

    :param hours:       Кол-во отработанных часов
    :param hour_cost:   Стоимость одного трудо-часа
    :param extra_pay:   Дополнительные выплаты
    :return:            Результат вычисления: часы * стоимость часа + доп. выплаты
    """

    hours, hour_cost, extra_pay = argv
    try:
        hours = float(hours)
        hour_cost = float(hour_cost)
        extra_pay = float(extra_pay)
    except ValueError:
        return None

    print(f'Wage: {hours * hour_cost + extra_pay}')
    return None
    # return hours * hour_cost + extra_pay
