# a = [1,2,3]
# b = a
#
# a[0] = 100
#
# print(a, b)

# a = [1, 2, 3]
# b = a[:]
#
# a[0] = 100
# print(a, b)

# a = [1, 2, 3, 4, 5]
#
# for i in a[:]:
#     print(i)
#     a.remove(i)

# import copy
#
# a = [1, 2, 3, [100]]
# b = copy.deepcopy(a)
#
# a[3][0] = 200
#
# print(a, b)

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# print(list(zip(*a)))

# for line in a:
#     for i in line:
#         print(i)

# name = input('Р’РІРµРґРёС‚Рµ РёРјСЏ:')
# print(name or 'Р“РѕСЃС‚СЊ')

# age = int(input('Р’РІРµРґРёС‚Рµ РІРѕР·СЂР°СЃС‚:'))
# РўРµСЂРЅР°СЂРЅС‹Р№ РѕРїРµСЂР°С‚РѕСЂ
# print('РџСЂРѕС…РѕРґРёС‚Рµ!' if age >= 18 else 'Р’Р°Рј РЅРµР»СЊР·СЏ!')

# a = 10
# b = 5+5
# print(a is b)
#
# a = 11
# print(a is b)
# print(id(a))

# import random
#
# my_list = []
# for _ in range(10):
#     my_list.append(random.randrange(-100, 100))
#
# print(my_list)
# # Р“РµРЅРµСЂР°С‚РѕСЂРЅРѕРµ РІС‹СЂР°Р¶РµРЅРёРµ
# my_list = [random.randrange(-100, 100) for _ in range(10)]
# my_list = [i ** 2 for i in range(-100, 10) if i > 0]
# print(my_list)

# a = {'name': 'Vasya'}
# if a.get('name') is None:
#     print('failed')


# my_dict = {i: i**2 for i in range(10)}
# print(my_dict)


# string = r'hello \' world'
# print(string)

# import re
#
# string = 'This is a test message p@ssw0rd'
# pattern = 'p.+rd$'
# print(re.search(pattern, string))
# print(re.findall(pattern, string))

# string = 'Hello world it is amazing it day!'
# pattern = 'world [a-z]{2} is'
# print(re.findall(pattern, string))

# try:
#     100 / 1
#     age = int(input('Р’РІРµРґРёС‚Рµ РІРѕР·СЂР°СЃС‚!'))
# except ZeroDivisionError:
#     print('РќР° РЅРѕР»СЊ РґРµР»РёС‚СЊ РЅРµР»СЊР·СЏ!')
# except ValueError:
#     print('Р’С‹ РІРІРµР»Рё РЅРµ С‡РёСЃР»Рѕ!')

try:
    f = open('1.txt')
    1/1
except FileNotFoundError:
    print('Р¤Р°Р№Р»Р° РЅРµ СЃСѓС‰РµСЃС‚РІСѓРµС‚ СЃ С‚Р°РєРёРј РёРјРµРЅРµРј!')
except ZeroDivisionError:
    print('РЅР° РЅРѕР»СЊ РґРµР»РёС‚СЊ РЅРµР»СЊР·СЏ!')
else:
    print('Try РѕС‚СЂР°Р±РѕС‚Р°Р» СѓСЃРїРµС€РЅРѕ, РёСЃРєР»СЋС‡РµРЅРёР№ РЅРµ РІРѕР·РЅРёРєР»Рѕ')
finally:
    print('РЇ РѕС‚СЂР°Р±РѕС‚Р°СЋ РІ Р»СЋР±РѕРј СЃР»СѓС‡Р°Рµ!')
    try:
        f.close()
    except NameError:
        pass

print('Р­С‚Р° С‡Р°СЃС‚СЊ РїСЂРѕРіСЂР°РјРјС‹ РєСЂРёС‚РёС‡РЅР°СЏ! РћРЅР° РґРѕР»Р¶РЅР° РІС‹РїРѕР»РЅСЏС‚СЊСЃСЏ РІ Р»СЋР±РѕРј СЃР»СѓС‡Р°Рµ!')