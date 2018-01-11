# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

create_dir = input('Хотите создать папки dir_1 dir_9? [Y/N]').upper()

if create_dir == 'Y':
    for x in range(1, 10):
        try:
            os.mkdir('dir_' + str(x))
        except FileExistsError:
            print("Папка существует")
else:
    print('Ну и ладно')

delete_dir = input('Хотите удалить папки dir_1 dir_9?').upper()

directory_list = os.listdir()

if delete_dir == 'Y':
    for x in directory_list:
        if os.path.isdir(x):
            try:
                os.rmdir(x)
            except OSError:
                print('Папка {} не пустая, папка не удалена'.format(x))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dir_list():
    list_of_dir = sorted(os.listdir())
    for elem in list_of_dir:
        if os.path.isdir(elem):
            print(elem + '\n')
        else:
            pass


dir_list()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

shutil.copy('hw05_easy.py','hw05_easy_copy.py')