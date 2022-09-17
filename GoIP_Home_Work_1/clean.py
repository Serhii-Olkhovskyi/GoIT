from pathlib import Path
import shutil
import sys


def file_remove(file_ob):  # Разбрасываем файлы по папкам
    if file_ob.suffix in list_zip:
        files_unpack(file_ob)
    elif file_ob.suffix in list_doc:
        new_folder = way_console.joinpath(list_name_folder[0])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    elif file_ob.suffix in list_image:
        new_folder = way_console.joinpath(list_name_folder[1])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    elif file_ob.suffix in list_music:
        new_folder = way_console.joinpath(list_name_folder[2])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    elif file_ob.suffix in list_video:
        new_folder = way_console.joinpath(list_name_folder[3])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    else:
        new_folder = way_console.joinpath(list_name_folder[5])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)


def files_unpack(file_ob):  # Распаковка архива
    folder_archive = way_console.joinpath(list_name_folder[4])
    shutil.unpack_archive(file_ob, folder_archive)
    file_ob.unlink()


def folder_create(way_consoles):
    # Создаем папки для файлов по группам
    new_folders(list_name_folder[0], way_consoles)
    new_folders(list_name_folder[1], way_consoles)
    new_folders(list_name_folder[2], way_consoles)
    new_folders(list_name_folder[3], way_consoles)
    new_folders(list_name_folder[4], way_consoles)
    new_folders(list_name_folder[5], way_consoles)


def folders_dell(way_consoles):  # Удаление папок
    for folder in way_consoles.glob('*'):
        if folder.name not in list_name_folder:
            shutil.rmtree(folder)


def list_of_files(way_consoles):
    print(f'Папка {list_name_folder[0]} содержит следующие файлы: ')
    print('')
    for folder in way_consoles.joinpath(list_name_folder[0]).glob('*'):
        print(folder.name)
    print('')
    print('-------------------------------------------------------')
    print(f'Папка {list_name_folder[1]} содержит следующие файлы: ')
    print('')
    for folder in way_consoles.joinpath(list_name_folder[1]).glob('*'):
        print(folder.name)
    print('')
    print('-------------------------------------------------------')
    print(f'Папка {list_name_folder[2]} содержит следующие файлы: ')
    print('')
    for folder in way_consoles.joinpath(list_name_folder[2]).glob('*'):
        print(folder.name)
    print('')
    print('-------------------------------------------------------')
    print(f'Папка {list_name_folder[3]} содержит следующие файлы: ')
    print('')
    for folder in way_consoles.joinpath(list_name_folder[3]).glob('*'):
        print(folder.name)
    print('')
    print('-------------------------------------------------------')
    print(f'Папка {list_name_folder[4]} содержит следующие файлы: ')
    print('')
    for folder in way_consoles.joinpath(list_name_folder[4]).glob('*'):
        print(folder.name)
    print('')
    print('-------------------------------------------------------')
    print(f'Папка {list_name_folder[5]} содержит следующие файлы: ')
    print('')
    for folder in way_consoles.joinpath(list_name_folder[5]).glob('*'):
        print(folder.name)
    print('')
    print('======================================================')
    print(f'Скрипту известны следующие расширения: {list_other} ')
    print('')
    print('======================================================')
    print(f'Скрипту не известны следующие расширения: ')
    for folder in way_consoles.joinpath(list_name_folder[5]).glob('*'):
        print(folder.suffix)


def main():  # считываем путь к папке с консоли
    return sys.argv[1]


def new_folders(name_folder, way_consoles):  # Функция создает папки если их нет
    document_folder = way_consoles / name_folder
    if not document_folder.is_dir():
        Path(document_folder).mkdir()


def translate(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ !#$%&'()*+,-./:;<=>?@[\]^`{|}~"

    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
                   "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", '_', '_',
                   '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                   '_', '_', '_', '_', '_', '_', '_', '_', '_')

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    new_name = name.translate(TRANS)  # out str
    return new_name


def normalize(way_consoles):  # Функция по переименовыванию файлов и папок
    for element in way_consoles.rglob('*/*'):
        if element.is_file():
            file_suffix = element.suffix
            new_file = translate(str(element.stem))
            rez_name = ''.join([new_file, file_suffix])
            element.replace(element.parent / rez_name)
        elif element.is_dir():
            new_file = translate(str(element.stem))
            element.replace(element.parent / new_file)


def parsing(way_consoles):  # Рекурсивно проходимся по папкам и передаем файлы в функцию file_remove
    for file_ob in way_consoles.glob('*'):
        if file_ob.is_file():
            file_remove(file_ob)
        elif file_ob.is_dir():
            parsing(file_ob)


if __name__ == '__main__':
    print('----------------------START----------------------')
    list_doc = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
    list_image = ['.jpeg', '.png', '.jpg', '.svg', '.JPG']
    list_music = ['.mp3', '.ogg', '.wav', '.amr']
    list_video = ['.avi', '.mp4', '.mov', '.mkv']
    list_zip = ['.zip', '.gz', '.tar']
    list_other = list_doc + list_image + list_music + list_video + list_zip
    list_name_folder = ['Documents', 'Images', 'Musics', 'Videos', 'Archives', 'Others']

    way_console = Path(main())

    folder_create(way_console)  # Создаем необходимые папки
    parsing(way_console)  # Проходимся по папкам
    folders_dell(way_console)  # Запускаем функцию для удаления пустых папок
    normalize(way_console)  # Запуск функции по переименовыванию файлов и папок
    list_of_files(way_console)  # Вывод результата работы
    print('----------------------FINISH---------------------')
