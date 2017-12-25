# print(abs(-100))
# print(round(1.1111, 2))
# print(sum([1, 2, 3, 4]))
# print(type(1))
# print(type('a'))
#
# for index, val in enumerate([1, 2, 3, 4]):
#     print(index, val)


def say_hello(name, surname):
    print('РџСЂРёРІРµС‚ {} {}'.format(name, surname))


# say_hello('Р’Р°РЅСЏ', 'РџРµС‚СЂРѕРІ')


# def summ(a, b):
#     return [a + b, a, b]

# print(summ(100, 200))

# c = 0
#
# def some_do():
#     c = 100
#     print(c)


# def average(*args):
#     summ = sum(args)
#     return summ/len(args)
#
# a = [1,2,3,4,5,6]
# print(a)
# print(*a)
# print(average(a))
# print(average(*a))

# def person_render(is_admin=False, **kwargs):
#     if is_admin:
#         print('Hello Admin!')
#     print('{} {} {}'.format(kwargs['name'], kwargs['surname'], kwargs['age']))
#
#
# person = {'name': 'Vasya', 'surname': 'Pupkin', 'age': 10}
# person_render(True, **person)

# a = ['Vasya', 'Ivan', 'Oleg']
# c = ['Pupkin', 'Ivanov']
# b = [100]
# print(list(zip(a, c, b)))

def my_func(x):
    return x ** 2


my_lambda_function = lambda x: x ** 2
my_list = [1, 2, 3, 4, 5, 6]

result = []
for i in my_list:
    result.append(i ** 2)


def send_data_to_server(data):
    print('sending data to server.... {}'.format(data))


# list(map(send_data_to_server, my_list))
# print(list(filter(lambda x: x > 0, [-1, -2, 1, 2])))

# f = open('log1.txt', 'r')
# print(f.readlines())
# f.write('100\n')
# f.close()

import os

path = os.path.join('files', 'test.txt')
print(path)

with open('log1.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line)