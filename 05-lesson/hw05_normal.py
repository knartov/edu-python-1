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

import os
from easy import dir_list


def main():
    print("Python util")

    answer = ''

    while answer != 'q':
        answer = input("Давайте поработаем? (Y/N/q)")
        if answer == 'Y':
            print("Отлично, хозяин!")
            print("Я умею:")
            print(" [1] - Перейти в папку")
            print(" [2] - Просмотреть содержимое текущей папки")
            print(" [3] - Удалить папку")
            print(" [4] - Создать папку")

            do = int(input("Укажите номер действия: "))

            if do == 1:
                print(os.listdir())

            elif do == 2:
                print()

            elif do == 3:
                print(psutil.pids())

            elif do == 4:
                print("=Дублирование файлов в текущей директории=")
                duble_files('.')

            else:
                pass

        elif answer == 'N':
            print("До свидания!")
            break
        else:
            print("Неизвестный ответ")


if __name__ == "__main__":
    main()


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
