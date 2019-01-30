# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

def dir_creation(nums = 0, name = 'dir_', path = '.'):
    if nums == 0:
        os.mkdir(path + "\\" + name)
    else:
        for i in range(nums):
            os.mkdir(path + "\\" + name + str(i))
def dir_removing(nums = 0, name = 'dir_', path = '.'):
    if nums == 0:
        os.rmdir(path + "\\" + name)
    else:
        for i in range(nums = 1, name = 'dir_', path = '.'):
            os.rmdir(path + "\\" + name + str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_direct(i = 'dirs'):
    f = []
    for (dirpath, dirnames, filenames) in os.walk('.'):
        if i == 'dirs':
            f.extend(dirnames)
            break
        elif i == 'files':
            f.extend(filenames)
            break
    return f

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def duplicate_file():
    filename = os.path.basename(__file__)
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
