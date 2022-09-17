# ------------- Задача № 8 -------------


"""Онлайн-магазин "У Бобра" предоставляет услугу экспресс-доставки для своих товаров по цене 5¤ за первый товар в заказе
и 2¤ – за все последующие товары. Необходимо реализовать функцию, принимающую в качестве первого параметра количество
товаров в заказе quantity, также должен присутствовать параметр, передаваемый только по ключу discount.
Параметр discount по умолчанию имеет значение 0 - скидки нет. Принимает значения от 0 до 1. Функция cost_delivery
возвращает общую сумму доставки с учётом скидки.
Надо предусмотреть, что функция cost_delivery при вызове может принимать любое количество позиционных аргументов.
"""


def cost_delivery(quantity, *_, discount=0):
    delivery_by_2 = quantity - 1
    if discount > 0:
        sum_delivery = (5 + delivery_by_2 * 2) * discount
        return sum_delivery
    else:
        sum_delivery = (5 + delivery_by_2 * 2)
        return sum_delivery


rez = cost_delivery(2, 1, 2, 3)
print(rez)


# ------------- Задача № 9 -------------
#
# Для функции из предыдущей задачи создайте строки документации. Можно использовать следующий шаблон


def cost_delivery(quantity, *_, discount=0):
    """Функция возвращает общую сумму доставки.

    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""

    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result


# ------------- Задача № 10 -------------
#
#
# Мы проводим розыгрыш призов среди первых 50 подписчиков ютуб-канала. У нас есть 7 призов для розыгрыша.
# Может возникнуть вопрос, сколько различных списков победителей мы можем получить при розыгрыше?
# Для этого мы будем использовать формулу сочетаний без повторений
# Cnk = n! / ((n - k)! · k!)
# где n — это общее количество людей (случаев), а k — количество людей, получивших призы.
# Напишите функцию number_of_groups, которая принимает параметры n и k, и с помощью функции factorial возвращает нам,
# сколько различных списков победителей мы можем получить при розыгрыше
#
# Примечание: Обратите внимание, какие большие значения мы получаем для факториала. Рекурсивные выражения надо всегда
# применять с осторожностью при вычислениях, чтобы не получить переполнение.

def factorial(n):
    k = 7
    return number_of_groups(n, k)


def number_of_groups(n, k):
    n_k = n - k
    rez_n_factor = 1
    rez_k_factor = 1
    rez_n_k_factor = 1
    factorial_n = True
    factorial_k = True
    factorial_n_k = True

    while factorial_n_k:
        if n_k < 2:
            factorial_n_k = False
        rez_n_k_factor = rez_n_k_factor * n_k
        n_k = n_k - 1

    print(f'rez_n_k_factor: {rez_n_k_factor}')

    while factorial_n:
        if n < 2:
            factorial_n = False
        rez_n_factor = rez_n_factor * n
        n = n - 1

    print(f'rez_n_factor: {rez_n_factor}')

    while factorial_k:
        if k < 2:
            factorial_k = False
        rez_k_factor = rez_k_factor * k
        k = k - 1

    print(f'rez_k_factor: {rez_k_factor}')

    result = int(rez_n_factor / (rez_n_k_factor * rez_k_factor))
    print(f'rez: {result}')
    return result


a = factorial(50)
print(f'Result: {a}')


# ------------- Задача № 11 -------------

# Одна из классических задач на понимание рекурсии, которую часто задают на собеседованиях, особенно начинающим
# программистам — это ряд Фибоначчи.
# Ряд Фибоначчи — это последовательность чисел вида: 0, 1, 1, 2, 3, 5, 8, ... где каждое следующее число
# последовательности получается сложением двух предыдущих членов ряда.
# В общем виде для вычисления n-го члена ряда Фибоначчи нужно вычислить выражение: Fn = Fn-1 + Fn-2.
# Эту задачу можно решить рекурсивно, вызывая функцию, вычисляющую числа последовательности до тех пор, пока вызов не
# дойдет до членов ряда меньше n = 1, где последовательность задана.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


rez = fibonacci(9)
print(rez)


def prepare_data(data):
    print(f'data: {data}')
    sort_list = sorted(data)
    print(f'sort_list: {sort_list}')
    sort_list.pop(0)
    sort_list.pop()
    return sort_list


rez = prepare_data([1, -3, 4, 100, 0, -5, 10, 1, 1])
print(rez)
