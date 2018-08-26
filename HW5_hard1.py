# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - смена директории")
    print("ls - отображение полного пути и содержимого текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        copy(file_name, 'copy' + file_name)
        print('файл {} скопирован'.format(file_name))
    except FileExistsError:
        print('Не удалось скопировать файл {}'.format(dir_name))

def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    choice = input('Вы действительно хотите удалить файл {}? да/нет'.format(file_name))
    if choice == 'да':
        try:
            os.remove(file_name)
            print('файл {} успешно удален'.format(file_name))
        except FileExistsError:
            print('файла {} не существует'.format(dir_name))
    else:
        print('Удаление отменено')

def change_directory():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print('Переход в директорию {} успешно осуществлен'.format(file_name))
    except FileExistsError:
        print('Не удалось перейти в директорию {}'.format(dir_name))

def full_path():
    os.path.abspath(os.getcwd())

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_directory,
    "ls": full_path,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

