# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import easy

def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        print('Успешно перешел!')
    except:
        print('Невозможно перейти!')

while True:
    try:
        choice = int(input('Выберите пункт меню:\n' +
                           '1. Перейти в папку\n' +
                           '2. Просмотреть содержимое текущей папки\n' +
                           '3. Удалить папку\n' +
                           '4. Создать папку\n' +
                           '_______________________________________\n' +
                           'Ваш выбор: '))
    except ValueError:
        print('Введите только число!')
        continue

    if choice == 3 or choice == 4:
        name_folder = input('Введите название папки: ')

    if choice == 1:
        path_folder = input('Введите полный путь папки: ')
        change_dir(path_folder)

    if choice == 2:
        easy.files_in_folder()

    if choice == 3:
        easy.delete_dir(name_folder)

    if choice == 4:
        easy.create_dir(name_folder)







