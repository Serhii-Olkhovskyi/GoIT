from string import *

# ---------- Задание №1 ----------
"""
Напишите функцию real_len, которая подсчитывает и возвращает длину строки без следующих управляющих
символов: [\n, \f, \r, \t, \v]

Для проверки правильности работы функции real_len ей будут переданы следующие строки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""
# --------------------------------------

# def real_len(text):
#
#     new_str = ""
#     out_list = "\n, \f, \r, \t, \v"
#
#     for i in text:
#         if i not in out_list:
#             new_str += i
#
#     len_new_str = len(new_str)
#     return len_new_str
#
# rez = real_len('Alex\nKdfe23\t\f\v.\r')
# print(rez)

# ---------- Задание №2 ----------
"""
У вашей компании есть блог. И надо реализовать функцию find_articles для поиска по статьям нашего блога. 
Есть список articles_dict, в котором находится описание статей блога. Каждый элемент этого списка представляет 
собой словарь со следующими ключами: фамилии авторов – ключ "author", название статьи – ключ "title", год 
издания – ключ "year".

Реализуйте функцию find_articles,

Параметр key функции определяет сочетание букв для поиска. Например, при key="Python" функция определяет, имеются 
ли в списке articles_dict статьи, в названии или именах авторов которых встречается это сочетание букв. Если такие 
элементы списка были найдены, то надо вернуть новый список из словарей, содержащий фамилии авторов, название и год 
издания всех таких статей.

Второй ключевой параметр функции letter_case определяет, учитывается ли при поиске регистр букв, по умолчанию он 
равен False и регистр не имеет значения т.е. "Python" и "python" это одно и тоже в тексте. Иначе искать полное 
совпадение.
"""
# --------------------------------------

# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]
#
#
# def find_articles(key, letter_case=False):
#     print('--------------------------')
#     print(key, letter_case)
#     print('--------------------------')
#     res_list = []
#     if letter_case:
#         for value in articles_dict:
#             if (key in value['title']) or (key in value['author']):
#                 res_list.append(value)
#         print(res_list)
#         return res_list
#     else:
#         key = key.lower()
#         print(key)
#         for value in articles_dict:
#             value['title'] = value['title'].lower()
#             value['author'] = value['author'].lower()
#             if (key in value['title']) or (key in value['author']):
#                 res_list.append(value)
#
#         print(res_list)
#         return res_list
#
#
# a = find_articles('Silver')
# print("__________________")
# print(f'res: {a}')

# ---------- Задание №3 ----------
"""
Ваша компания проводит маркетинговые кампании с помощью SMS рассылок. Автоматический сбор телефонных номеров с базы 
данных формирует определенный список. Но клиенты оставляют свои номера в произвольном виде:

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
Сервис рассылок прекрасно понимает и может отправить SMS-ку клиенту, только если телефонный номер содержит цифры. 
Необходимо реализовать функцию sanitize_phone_number, которая будет принимать строку с телефонным номером и 
нормализовать его, т.е. будет убирать символы (, -, ), + и пробелы.

Результат:

380501233234
0503451234
0508889900
380501112222
380501112211
"""
# --------------------------------------

# def sanitize_phone_number(phone):
#     element = '0123456789'
#     new_phone = ''
#     for elem in phone:
#         if elem in element:
#             new_phone += elem
#     print(new_phone.strip())
#     return (new_phone.strip())
#
# sanitize_phone_number('+38(050)123 - 32 - 34')

# ---------- Задание №4 ----------
"""
В модуле работы с функциями мы писали функцию get_fullname для составления полного имени. Выполним небольшое 
продолжение задачи и напишем функцию is_check_name, которая принимает два параметра (fullname, first_name) и возвращает 
логическое True или False. Это результат проверки, является ли строка first_name префиксом строки fullname. 
Функция is_check_name строго относится к регистру букв, то есть «Sam» и «sam» для неё разные имена.
"""
# --------------------------------------

# def is_check_name(fullname, first_name):
#     if fullname.startswith(first_name):
#         return True
#     else:
#         return False

# ---------- Задание №5 ----------
"""
Вернемся к нашей задаче с телефонными номерами. Компания расширяется и вышла на рынок Азии. 
Теперь в списке приходят телефоны разных стран. Каждая страна имеет свой телефонный код .

Компания работает со следующими странами

Страна	    Код ISO	Префикс
Japan	    JP	+81
Singapore	SG	+65
Taiwan	    TW	+886
Ukraine	    UA	+380
Чтобы мы могли корректно выполнить маркетинговую SMS кампанию, необходимо выдать для каждой страны свой список 
телефонных номеров.

Напишите функцию get_phone_numbers_for_сountries, которая будет:

Принимать список телефонных номеров.
Санитизировать (нормализовать) полученный список телефонов клиентов с помощью нашей функции sanitize_phone_number.
Сортировать телефонные номера по указанным в таблице странам.
Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
{
    "UA": [<здесь список телефонов>],
    "JP": [<здесь список телефонов>],
    "TW": [<здесь список телефонов>],
    "SG": [<здесь список телефонов>]
}
Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в список словаря с ключом "UA".
"""

# --------------------------------------
# def sanitize_phone_number(phone):
#     print(f'phone: {phone}')
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     print(f"new_phone: {new_phone}")
#     return new_phone
#
#
# def get_phone_numbers_for_countries(list_phones):
#     phone_dict = {
#         'JP': [],
#         'SG': [],
#         'TW': [],
#         'UA': []
#     }
#     print(f'list_phones: {list_phones}')
#     for i in list_phones:
#         new_phone = sanitize_phone_number(i)
#         if new_phone.startswith('81'):
#             phone_dict['JP'].append(new_phone)
#         elif new_phone.startswith('65'):
#             phone_dict['SG'].append(new_phone)
#         elif new_phone.startswith('886'):
#             phone_dict['TW'].append(new_phone)
#         else:
#             phone_dict['UA'].append(new_phone)
#
#     print(f'phone_dict: {phone_dict}')
#     return phone_dict

# ---------- Задание №6 ----------
"""
Рассмотрим задачу на проверку спама в email письме или фильтрацию запрещенных слов в сообщении.

Пусть функция is_spam_words принимает строку (параметр text), проверяет её на содержание запрещённых слов из списка 
(параметр spam_words), и возвращает результат проверки: True, если есть хоть одно слово из списка, и False, если в 
тексте стоп-слов не обнаружено.

Слова в параметре text могут быть в произвольном регистре, а значит функция is_spam_words, при поиске запрещённых слов, 
регистронезависима и весь текст должна сводить к нижнему регистру. Для упрощения, будем считать, что в строке 
присутствует только одно запрещенное слово.

Предусмотреть третий параметр функции space_around, который по умолчанию равен False. Он отвечает за то, что функция 
будет искать отдельное слово или нет. Слово считается стоящим отдельно, если слева от слова находится символ пробела 
или оно расположено в начале текста, а справа от слова находится пробел или символ точки.

Например, в тексте мы ищем слово "лох". То в слове "Молох" вызов и результат будет следующим:

print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
т.е. во втором случае слово не отдельное и является частью другого.

В этом примере, функция вернет True в обоих случаях.
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
"""

# --------------------------------------

# def is_spam_words(text, spam_words, space_around=False):
#     print(f'text: {text}, spam_words: {spam_words}, space_around: {space_around}')
#     text = text.lower()
#     spam_words = str(spam_words)
#     new_spam = (
#                 spam_words.replace("[", "")
#                     .replace("]", "")
#                     .replace("'", "")
#             )
#
#     index_new_spam = int(text.index(new_spam))
#     len_new_spam = int(len(new_spam))
#
#     if not space_around:
#         spam_word = text.find(new_spam)
#         if spam_word == -1:
#             return False
#         else:
#             return True
#     else:
#         if text[index_new_spam - 1] == ' ' and text[index_new_spam+len_new_spam] == ' ':
#             return True
#         elif text[index_new_spam - 1] == ' ' and text[index_new_spam + len_new_spam] == '.':
#             return True
#         elif text.startswith(new_spam):
#             return True
#         else:
#             return False
#
# print(is_spam_words('лох бог ужасен.', ['лох'], space_around = True))

# ---------- Задание №7 ----------
"""
Вы уже научились работать со строками более глубоко и теперь у вас есть полный набор инструментов для обработки 
строк с помощью Python.

С помощью функции zip, по аналогии с примером из теории, создайте словарь TRANS для транслитерации. Создавайте словарь 
TRANS вне функции translate

Напишите функцию translate, которая проводит транслитерацию кириллического алфавита на латинский.

Функция translate:

принимает на вход строку и возвращает строку;
проводит транслитерацию кириллических символов на латиницу;
Пример работы:

print(translate("Дмитрий Коробов"))  # Dmitrij Korobov
print(translate("Александр Иванович"))  # Aleksandr Ivanovich
Примечание: В задаче, при создании словаря TRANS, код TRANS[ord(c.upper())] = l.title() будет считаться не правильным, 
а TRANS[ord(c.upper())] = l.upper() — правильным. Это компромисс, так как в первом случаем мы учитываем заглавные 
буквы, а во втором — правильно, если имя будет все заглавными буквами. Чтобы не усложнять задачу, принято как в 
документах — все имя печатается заглавными.
"""

# --------------------------------------

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
               "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
print(TRANS)


def translate(name):
    print(name.translate(TRANS))


print(translate('Серж'))

# ---------- Задание №8 ----------
"""
В прошлом модуле мы работали с системой оценок ECTS. Напишите функцию formatted_grades, которая принимает на вход 
словарь оценивания студентов по предмету следующего вида:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
И возвращает список отформатированных строк, чтобы при выводе следующего кода:

for el in formatted_grades(students):
    print(el)
Получалась следующая таблица:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
первый столбец — ширина 4 символа, выравнивание по правому краю
второй столбец — ширина 10 символов, выравнивание по левому краю
третий и четвертый столбец — ширина 5 символов и выравнивание по центру
вертикальный символ | не входит в ширину столбца
"""

# --------------------------------------

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#
# def formatted_grades(students):
#     f_students = []
#     index = 1
#     for key, student_grade in students.items():
#         grade = grades.get(student_grade)
#         print(f'grade: {grade}')
#         f_students.append("{:>4}|{:<10}|{:^5}|{:^5}".format(index, key, student_grade, grade))
#         index += 1
#         print(f_students)
#     return f_students
#
# print(formatted_grades({'Nick': 'A', 'Olga': 'B', 'Boris': 'FX', 'Anna': 'C'}))

# ---------- Задание №9 ----------
"""
Поработаем немного со спецификацией в форматировании строк. Напишите функцию formatted_numbers, которая возвращает 
список отформатированных строк, чтобы при выводе следующего кода:

for el in formatted_numbers():
    print(el)
Получалась следующая таблица:

| decimal  |   hex    |  binary  |
|0         |    0     |         0|
|1         |    1     |         1|
|2         |    2     |        10|
|3         |    3     |        11|
|4         |    4     |       100|
|5         |    5     |       101|
|6         |    6     |       110|
|7         |    7     |       111|
|8         |    8     |      1000|
|9         |    9     |      1001|
|10        |    a     |      1010|
|11        |    b     |      1011|
|12        |    c     |      1100|
|13        |    d     |      1101|
|14        |    e     |      1110|
|15        |    f     |      1111|
все столбцы имеют ширину в 10 символов
у заголовков таблицы выравнивание по центру
первый столбец десятичных чисел — выравнивание по левому краю
второй столбец шестнадцатеричных чисел — выравнивание по центру
третий столбец двоичных чисел — выравнивание по правому краю
вертикальный символ | не входит в ширину столбца
Как вы уже поняли, функция formatted_numbers выводит таблицу чисел от 0 до 15 в десятичном, шестнадцатеричном и 
двоичном формате.
"""

# --------------------------------------

# def formatted_numbers():
#     f_numbers = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
#     for i in range(16):
#         f_numbers.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))
#         print(f_numbers)
#     return f_numbers


# ---------- Задание №10 ----------
"""
Напишите функцию find_word, которая принимает два параметра: первый text и второй word. Функция выполняет поиск 
указанного слова word в тексте text с помощью функции search и возвращает словарь.

При вызове функции:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and 
    first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат должен быть следующего вида при совпадении:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming 
    language, and first released it in 1991 as Python 0.9.0.'
}
где

result — результат поиска True или False
first_index — начальная позиция совпадения
last_index — конечная позиция совпадения
search_string — часть строки, в которой было совпадение
string — строка, переданная в функцию
Если совпадений не обнаружено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and 
    first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming 
    language, and first released it in 1991 as Python 0.9.0.'
}
"""

# --------------------------------------

import re

#
# def find_word(text, word):
#     result_dict = {
#         'result': False,
#         'first_index': None,
#         'last_index': None,
#         'search_string': word,
#         'string': text
#
#     }
#
#     search_string = re.search(word, text)
#
#     if search_string:
#         index_word = search_string.span()
#         result_dict['result'] = True
#         result_dict['first_index'] = index_word[0]
#         result_dict['last_index'] = index_word[-1]
#
#     return result_dict
#
#
# print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor Python to the", "Python"))

# ---------- Задание №11 ----------
"""
Для закрепления материала напишите функцию find_all_words, которая ищет совпадение слова в тексте. Функция возвращает 
список всех нахождений слова в параметре word в тексте в любом виде написания, т.е. например, возможные варианты 
написания слова "Python" как pYthoN, pythOn, PYTHOn и т.д. главное, чтобы сохранялся порядок слов, регистр не имеет 
значение.

Подсказка: функции модуля re принимают еще последний параметр flags и мы можем определить нечувствительность к 
регистру, присвоив ему значение re.IGNORECASE
"""

# --------------------------------------

# def find_all_words(text, word):
#
#     res = re.findall(word, text, re.IGNORECASE)
#
#     return res
#
#
#
# string = '''
# Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and
# first released pYthoN it in 1991 as Python 0.9.0. pythOn
# '''
# 
# search_string = "Python"
#
# print(find_all_words(string, search_string))

# ---------- Задание №12 ----------
"""
В шестой задаче мы писали функцию is_spam_words, которая определяла, есть или нет стоп-слова в тексте сообщения. 
Давайте пойдем дальше и применим функцию sub модуля re для замены указанных в списке стоп-слов на некоторый шаблон. 
Например, все "плохие" слова будем заменять звездочками. Напишите функцию replace_spam_words, которая принимает строку 
(параметр text), проверяет её на содержание запрещённых слов из списка (параметр spam_words), и возвращает результат 
строку, но вместо запрещенных слов, подставлен шаблон из *, причем длина шаблона равна длине запрещенного слова. 
Определить нечувствительность к регистру стоп-слов.
"""

# --------------------------------------

# def replace_spam_words(text, spam_words):
#     re.IGNORECASE = True
#     for word in spam_words:
#         text = re.sub(word, len(word) * '*', text)
#     return text
#
#
# stop_words = ['began', 'Python']
# string = '''
# Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and
# first released pYthoN it in 1991 as Python 0.9.0. pythOn
# '''
# print(replace_spam_words(string, stop_words))

# ---------- Задание №13 ----------
"""
Теперь мы потренируемся писать полезные регулярные выражения. Напишите регулярное выражение для функции 
find_all_emails, которая будет в тексте (параметр text) находить все email и возвращать список полученных из текста 
совпадений.

В целях упрощения примем, что:

алфавит, используемый для названия email, — английский
префикс (все, что находится до символа @) начинается с латинской буквы и может содержать любое число или букву, 
включая нижнее подчеркивание и символ точки, состоит минимум из двух символов
суффикс письма (все, что находится после символа @) состоит только из букв английского алфавита, состоит из двух 
частей, разделенных точкой, и доменное имя верхнего уровня не может быть меньше двух символов (все, что после точки)
Данное регулярное выражение ни в коей мере не претендует на покрытие всех возможных вариантов email.

При выполнении этого задания мы рекомендуем использовать следующий сервис для проверок регулярных выражений regex101.
"""

# --------------------------------------
#
# def find_all_emails(text):
#     result = re.findall(r"[a-zA-Z]\S{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
#     return result
#
#
# email = '''
# Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com
# abc111@test.com.net
# '''
# print(find_all_emails(email))

# ---------- Задание №14 ----------
"""
Задача будет похожа на предыдущую, но теперь в тексте мы будем искать номер телефона Украины в международном формате, 
шаблон которого следующий: +380(67)777-7-777 или +380(67)777-77-77

Напишите регулярное выражение для функции find_all_phones, которая будет в тексте (параметр text) находить все 
телефонные номера указанного шаблона и возвращать список полученных из текста совпадений.

В целях упрощения примем, что:

используем только цифры и символы +, (, ) и -
телефонный номер начинается с символа +
шаблон телефона символ + потом три цифры 380, символ (, две цифры, символ ), три цифры, символ -, одна или две цифры, 
символ -, две или три цифры
длина шаблона телефонного номера всегда 17 символов
Данное регулярное выражение ни в коей мере не претендует на покрытие всех возможных вариантов телефонных номеров.

При выполнении этого задания мы рекомендуем использовать следующий сервис для проверок регулярных выражений regex101.
"""

# --------------------------------------

# def find_all_phones(text):
#     result = re.findall(r"\+380\(\d{2}\)\d{3}\-(?:\d{1}\-\d{3}|\d{2}\-\d{2})", text)
#     return result
#
#
# phone_numbers = '''
# Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net
# +380(67)111-777-777+380(67)777-77-787
# '''
# print(find_all_phones(phone_numbers))

# ---------- Задание №15 ----------
"""
И последняя задача на регулярные выражения — это поиск в тексте гиперссылок.

Напишите регулярное выражение для функции find_all_links, которая будет в тексте (параметр text) находить все линки и 
возвращать список полученных из текста совпадений.

В целях упрощения примем, что:

начало гиперссылки может быть http:// или https://
доменное имя — это набор латинских букв, цифр, символов подчеркивания _ и точек .
символы точек . не могут встречаться рядом
Фактически в учебном примере мы будем искать простые url адреса:

https://www.google.com
https://www.facebook.com
https://github.com
Данное регулярное выражение ни в коей мере не претендует на покрытие всех возможных вариантов гиперссылок.

При выполнении этого задания мы рекомендуем использовать следующий сервис для проверок регулярных выражений regex101.
"""

# --------------------------------------
#
# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"[https]{4,5}[:\/\/]{3}[a-zA-Z]{1,3}[.]{0,1}[a-zA-Z]{1,}[.]{0,1}[a-zA-Z]{2,}", text)
#     for match in iterator:
#         result.append(match.group())
#     return result


# p = Path()
# print(p.parent)
# print(p.name)

