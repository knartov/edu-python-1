# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

create_dir = input('Хотите создать папки dir_1 dir_9? [Y/N]').upper()

if create_dir == 'Y':
    for x in range(1, 10):
        dir_list.append('dir_' + str(x))
        try:
            os.mkdir('dir_' + str(x))
        except FileExistsError:
            print("Папка существует")
else:
    print('Ну и ладно')

delete_dir = input('Хотите удалить папки dir_1 dir_9?').upper()

dir_list = os.listdir()
if delete_dir == 'Y':
    for x in dir_list:
        if os.path.isdir(x):
            os.rmdir(x)
        else:
            pass


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
