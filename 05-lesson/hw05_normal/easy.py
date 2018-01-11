# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def dir_list():
    '''
    Shows all files in current directory
    :return: nothing
    '''
    list_of_dir = sorted(os.listdir())
    for elem in list_of_dir:
        print(elem)


def chng_dir(dirname):
    '''
    Changes directory, gets folder name as a param
    :param dirname: name of folder in current directory
    :return: nothing
    '''
    if os.name == 'nt':
        os.chdir(os.getcwd() + '\{}'.format(dirname))
    else:
        os.chdir(os.getcwd() + '/{}'.format(dirname))

def del_dir(dirname):
    '''
    Deletes directory, gets folder name as a param
    :param dirname: name of folder in current directory
    :return: nothing
    '''
    os.rmdir(dirname)

def mk_dir(dirname):
    '''
    Creates directory, gets folder name as a param
    :param dirname: name of folder
    :return: nothing
    '''
    os.mkdir(dirname)
