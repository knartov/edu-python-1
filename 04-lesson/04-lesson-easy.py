# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

initial_list = map(lambda x: int(x), list(input('Введите числа через пробел: ').split()))

print(list(x ** 2 for x in initial_list))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# apple orange peach pineapple kiwi
# pineapple orange lemon banana mandarin

first_list = list(input('Введите первый список фруктов через пробел: ').split())
second_list = list(input('Введите второй список фруктов через пробел: ').split())

common_list = [elem for elem in second_list if elem in first_list]

print(common_list)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


initial_list = map(lambda x: int(x), list(input('Введите числа через пробел: ').split()))
final_list = [elem for elem in initial_list if elem >= 0 and elem % 3 == 0 and elem % 4 != 0]
print(final_list)
