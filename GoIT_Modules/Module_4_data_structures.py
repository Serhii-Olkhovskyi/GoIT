# ------------- Задача № 3 -------------
"""
 Напишите функцию format_ingredients, которая будет принимать на вход список из ингредиентов
 ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] и возвращать собранную строку из его элементов в описанный выше
 способ. Ваша функция должна уметь обрабатывать списки любой длины.
"""
# --------------------------------------

# def format_ingredients(items):
#     str_rez = ""
#     print(f'items: {items}')
#     str_len=len(items)
#     print(f'str_len: {str_len}')
#     last_element = items.pop(str_len-1)
#     print(f'last_element: {last_element}')
#     print(f'items_not_last_element: {items}')
#     str_rez = str(items)
#     print(f'str_items: {str_rez}')
#     # for i in items:
#     str_rez = ', '.join(items)
#     str_rez = f'{str_rez} and {last_element}'
#     return str_rez
#
#
# rez = format_ingredients(['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar'])
# print(f'RESULT_1: {rez}')
#
# print('===============================')
#
# myList = ['str1']
# myString = ' '.join(myList) # '' - разделитель между элементами списка соответственно
#
# print(myString)
# myString = '_'.join(myList)
#
# print(myString)
#
# print('===============================')
#
# def format_ingredients(items):
#     str_rez = ""
#     print(f'items: {items}')
#     str_len=len(items)
#     print(f'str_len: {str_len}')
#     last_element = items.pop(str_len-1)
#     print(f'last_element: {last_element}')
#     print(f'items_not_last_element: {items}')
#     str_rez = str(items)
#     print(f'str_items: {str_rez}')
#     # for i in items:
#     str_rez = ', '.join(items)
#     if str_len == 1:
#         return last_element
#     else:
#         str_rez = f'{str_rez} and {last_element}'
#         return str_rez
#
# rez = format_ingredients(['2 eggs'])
# print(f'RESULT_2: {rez}')

# ------------- Задача № 4 -------------
"""
 Реализуйте две функции. Первая будет использоваться в бухгалтерии при расчете стипендии, get_grade принимает 
 ключ в оценке ECTS, и должна возвращать соответствующую пятибалльную оценку (первый столбик таблицы). 
 Вторая get_description тоже принимает ключ в оценке ECTS, но будет возвращать объяснение оценки в текстовом формате 
 (последний столбик таблицы) и будет использоваться в электронной зачетке студента. На несуществующий ключ функции 
 должны возвращать значение None.
"""
# --------------------------------------

# def get_grade(key):
#     print(f'key_1: {key}')
#     lib_dictict = {'A': 5, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 'FX': 2, 'F': 1}
#     for i in lib_dictict:
#         if i == key:
#             print('IF - OK')
#             def_rez = lib_dictict[i]
#             return def_rez
#
#
# def get_description(key):
#     print(f'key_1: {key}')
#     lib_dictict = {'A': 'Perfectly', 'B': 'Very good', 'C': 'Good', 'D': 'Satisfactorily', 'E': 'Enough',
#                    'FX': 'Unsatisfactorily', 'F': 'Unsatisfactorily'}
#     for i in lib_dictict:
#         if i == key:
#             print('IF - OK')
#             def_rez = lib_dictict[i]
#             return lib_dictict[i]
#
#
# rez_v1 = get_grade('B')
# print(f'resoult: {rez_v1}')
# rez_v2 = get_description('A')
# print(f'resoult: {rez_v2}')

# ------------- Задача № 5 -------------
"""
Как мы уже знаем, ключ в словаре должен быть уникальным, а вот значение его нет. Реализуйте функцию lookup_key 
для поиска всех ключей по значению в словаре. Первым параметром в функцию мы передаем словарь, а вторым — значение, 
которое хотим найти. Таким образом результат может быть как список ключей, так и пустой список, если мы ничего 
не найдем.
"""
# --------------------------------------

# def lookup_key(data, value):
#     print(data, value)
#     resault_list = []
#     for key, values in data.items():
#         if values == value:
#             resault_list.append(key)
#
#     return resault_list
#
#
# input_dict = {'key1':1, 'key2':2, 'key3':3, 'key4':2}
# values = 2
# resault = lookup_key(input_dict, values)
# print(resault)

# ------------- Задача № 7 -------------
"""
Есть четырехугольная схема полетов дрона с координатами (1, 2, 3, 4). 
У нас есть словарь points, ключи которого — кортежи, точки полета между координатами четырехугольника, вида (1, 2). 
Значения словаря — это расстояния между указанными точками.

points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
Напишите функцию calculate_distance, которая на вход принимает список координат четырехугольника из словаря 
вида [0, 1, 3, 2, 0]. Функция должна подсчитать, используя указанный словарь, какое общее расстояние пролетит дрон, 
двигаясь между точками.

Примечания:

при взятии у словаря points значения, в ключ-кортеже всегда должна быть первой координата 
с меньшим значением — (2, 3), но не (3, 2);
для пустого списка и списка с одной координатой функция calculate_distance должна возвращать 0.
"""
# --------------------------------------

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }
#
#
# def calculate_distance(coordinates):
#
#     print(f'inp_coord: {coordinates}')
#     resault_sum = 0
#     inp_coord = []
#     if coordinates != 0:
#         for i in range(len(coordinates) - 1):
#             inp_coord.append(coordinates[i:i + 2])

# print(f'coord: {inp_coord}')
# for i in inp_coord:
#     resault_sum += points.get(i)
# print(resault_sum)

#
# else:
#     return resault_sum

#
# inp_coord = [0, 1, 3, 2, 0, 2]
# print(calculate_distance(inp_coord))

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }
#
#
# def calculate_distance(coordinates):
#     resault_sum = 0
#     if coordinates != 0:
#
#         list_one = []
#         inp_coord = []
#         tuple_inp_coord = []
#
#         for i in range(len(coordinates) - 1):
#             inp_coord.append(coordinates[i:i + 2])
#             for i in range(len(inp_coord)):
#                 if inp_coord[i][0] > inp_coord[i][1]:
#                     inp_coord[i][0], inp_coord[i][1] = inp_coord[i][1], inp_coord[i][0]
#
#         for ind in range(len(inp_coord)):
#             tuple_inp_coord.append(tuple(inp_coord[ind]))
#         print(f'tuple_inp_coord: {tuple_inp_coord}')
#
#         for i in tuple_inp_coord:
#             resault_sum += points.get(i)
#         return resault_sum
#     else:
#         return resault_sum
#
#
# inp_coord_user = [0, 1, 3, 2, 0, 2]
# print(calculate_distance(inp_coord_user))

# ------------- Задача № 8 -------------
"""
Необходимо написать функцию реализации следующего игрового алгоритма. На вход функции game подается два аргумента: 
список, состоящий из списков, и начальное значение power - энергия игрока. Внутренние списки — это списки с числовым 
значением энергии, которые может поглотить игрок, если они меньше или равные его энергии. После поглощения он 
двигается по списку дальше и, или поглощает список полностью до конца, или, если находит энергию выше собственной, 

Пример списка:

[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
Для этого списка и начальной энергии равной 1, игрок поглотит из первого списка первые два значения и покинет его, 
встретив значение 5, так как на этот момент будет обладать энергией в 3. Второй список пропустит сразу, а третий 
полностью поглотит и получит окончательную энергию в 6.
"""
# --------------------------------------
#
# def game(terra, power):
#     print(f'terra: {terra}')
#     print(f'start user power: {power}')
#     print('________________________')
#     terra_len_all = len(terra)
#     len_massive=[]
#     for i in range(len(terra)):
#         terra_len_lvl = len(terra[i])
#         len_massive.append(terra_len_lvl)
#     for i in range(len(terra)):
#         for lvl1 in range(len(terra[i])):
#             print(f'terra: {terra[i][lvl1]}')
#             if power >= terra[i][lvl1]:
#                 power += terra[i][lvl1]
#                 print(f'power in if: {power}')
#             else:
#                 print(f'power in else: {power}')
#                 break
#
#
#     return power
#
# game_rez = game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]],1)
# print('________________________')
# print(f'user_power: {game_rez}')

# ------------- Задача № 9 -------------
"""
Всем известно, что для доступа к кредитной карте банка необходим пин-код. Классически сложилось, что это сочетание 
четырех цифр. Нам необходимо решить следующую программистскую задачу. Есть подготовленный список пин-кодов. Напишите 
функцию is_valid_pin_codes, которая будет принимать в качестве параметра список этих пин-кодов — строка из четырех цифр, 
и возвращать логическое значение — валидный список или нет. Убедитесь в том, что среди этих пин-кодов в списке не будет 
дубликатов, все они хранятся в виде строк, их длина равна 4 символам и содержат они только цифры.

Пример аргумента для функции is_valid_pin_codes:

['1101', '9034', '0011']
Если список удовлетворяет всем поставленным условиям, функция возвращает логическое значение True. Если хоть одно из 
условий нарушено, возвращаемое значение — False. Предусмотреть проверку на пустой список в аргументе функции и 
вернуть False.
"""

# --------------------------------------

# def is_valid_pin_codes(pin_codes):
#     print(f'input data: {pin_codes}')
#     print('________________')
#     if pin_codes == []:  # проверка на пустой запрос
#         return False
#     for i in range(len(pin_codes)):  # проверка на длинну пин кода
#         if len(pin_codes[i]) != 4:
#             return False
#     set_input_data = set(pin_codes) # перевод в set
#     if len(pin_codes) != len(set_input_data): # проверка на повторение
#         return False
#     str_input_data = str(pin_codes)  # перевод в str
#     # Удаление ненужных знаков
#     str_input_data = str_input_data.replace('[','')
#     str_input_data = str_input_data.replace("'", '')
#     str_input_data = str_input_data.replace("]", '')
#     str_input_data = str_input_data.replace(",", '')
#     str_input_data = str_input_data.replace(" ", '')
#     #--------------------------
#     if str_input_data.isdigit() == False: # Проверка на числа
#         return False
#     print(f'str_input_data: {str_input_data}')
#     return True
#
# resault = is_valid_pin_codes(['1101', '9034', '0011'])
# print(f'resault function: {resault}')

# ------------- Задача № 10 -------------
"""
Браузер Chrome предлагает нам сгенерированные случайные пароли для сайтов и веб-приложений. 
Мы потренируемся решать подобные задачи. Разобьем ее на три этапа. Первый этап — создайте функцию get_random_password, 
которая будет генерировать случайную строку пароль.

Требования:

в пароле должно быть 8 символов.
для шифрования пароля будем использовать следующий набор символов:
()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
Эти символы лежат в пределах от 40 до 126 кода в таблице ASCII включительно, и доступ к ним можно получить с помощью 
функции chr.

chr(40)  # (
chr(126)  # ~
Чтобы получить случайное целое значение из заданного диапазона, мы используем стандартный модуль Python random и его 
функцию randint. Она имеет вызов вида randint(A, B) и возвращает случайное целое число N, A ≤ N ≤ B.

from random import randint

random_num = randint(40, 126)
После выполнения кода в random_num будет находиться случайное целое число от 40 до 126 включительно.

Таким образом функция get_random_password должна случайным образом выбрать из предложенного диапазона 8 символов и 
возвратить сгенерированный пароль в виде строки.
"""

# --------------------------------------

# from random import randint
#
#
# def get_random_password():
#     pozision = 0
#     sumbol_list = []
#     resault = []
#     sumbol_str = ""
#     while pozision < 8:
#         random_num = randint(40, 126)
#         sumbol_list.append(random_num)
#         pozision += 1
#     print(sumbol_list)
#     for i in sumbol_list:
#         resault.append(chr(i))
#     print(resault)
#     rez = ''.join(resault)
#     print(type(rez))
#     print(rez)
#     return rez
#
#
# print(get_random_password())
# ------------- Задача № 11 -------------
"""
Второй этап. Необходимо написать функцию is_valid_password, которая будет проверять полученный параметр — пароль на 
надежность.

Критерии надежного пароля:

Длина строки пароля восемь символов.
Содержит хотя бы одну букву в верхнем регистре.
Содержит хотя бы одну букву в нижнем регистре.
Содержит хотя бы одну цифру.
Функция is_valid_password должна вернуть True, если переданный в качестве параметра пароль отвечает требованиям 
надежности. В противном случае вернуть False.
"""

# --------------------------------------

# def is_valid_password(password):
#     item_int = '1234567890'
#
#     if len(password) < 8: # Проверка на длинну символов
#         return False
#     if password.lower() == password or password.upper() == password: # Проверка на наличие больштх букв
#         return False
#     if password.isdigit() or password.isalpha(): # Проверяет есть ли в пароле буквы и цифры
#         return False
#     for char in password: # Прокручиваем password и
#         if char in item_int: # проверяем есть ли цифра
#             return True # если есть - то пароль подходит
#
#     return False
#
#
# print(is_valid_password('z,qrE*IE'))
# print(is_valid_password('Qwerty-iop'))
# print(is_valid_password('Qwerty1iop'))
# print(is_valid_password('Qwertyiop'))
# print(is_valid_password('234567890'))

# ------------- Задача № 12 -------------
"""
И наконец третий, последний этап. Используя решения из предыдущих двух задач, напишите функцию get_password, 
которая сгенерирует нам случайный надежный пароль и вернет его. Алгоритм простой — мы генерируем пароль с помощью 
функции get_random_password и, если он проходит надежность проверкой функцией is_valid_password, возвращаем его, если 
нет — повторяем итерацию снова.

Примечание: Хорошей практикой будет ограничить количество попыток (например до 100), чтобы не получить бесконечный 
цикл.
"""

# --------------------------------------
# from random import randint
#
#
# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result
#
#
# def is_valid_password(password):
#     print(password)
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# def get_password():
#     key = True
#     elem = 0
#     list_pass = ""
#     while key:
#         new_pass = get_random_password()
#         valid = is_valid_password(new_pass)
#         if valid:
#             return new_pass
#             elem += 1
#             if elem == 100:
#                 key = False
#
#     print(list_pass)
#     return list_pass

# ------------- Задача № 13 -------------
"""
Напишите функцию parse_folder, она принимает единственный параметр path, который является объектом Path. Функция должна 
просканировать директорию path и вернуть кортеж из двух списков. Первый — это список файлов внутри директории, 
второй — список директорий.

Пример вывода функции:

(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 'module-06', 'module-07',
  'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])
"""

# --------------------------------------

# def parse_folder(path):
#     files = []
#     folders = []
#
#     for i in path.iterdir(): # Перебираем путь
#         if i.is_file() is True: # Если i является файтом,
#             files.append(i.name) #  то записываем в files
#         else:
#             folders.append(i.name) # иначе записываем в folders
#
#     return files, folders

# ------------- Задача № 14 -------------
"""
Создайте функцию parse_args, которая возвращает строку, составленную из аргументов командной строки, разделенных 
пробелами. Например, если скрипт был вызван командой: python run.py first second, то функция parse_args должна вернуть 
строку следующего вида "first second".
"""

# --------------------------------------

# import sys
#
#
# def parse_args():
#     result = ""
#     for arg in sys.argv:  # проходим по командной строке
#         result = result + ' ' + arg  # загоняем результат в строку
#     num_index = result.index(' ', 1)  # ищем индекс второго пробела, что б выкинуть имя файла
#     result = result[num_index + 1:]  # выкидываем имя файла по индексу
#
#     return result


from string import ascii_lowercase