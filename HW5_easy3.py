# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import os

copyfile = os.path.abspath('copy')
shutil.copy(__file__, copyfile)

