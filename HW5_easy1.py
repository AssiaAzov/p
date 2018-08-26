# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1,10):
    try:
        os.mkdir('dir_' + str(i))
    except FileExistsError:
        i += 1

for i in range(1,10):
    os.rmdir('dir_' + str(i))

