'''
5. Реализуйте алгоритм перемешивания списка.
'''

list = ['Машина', 'Колесо', 'Руль', 'Педали']
print(f'Исходный список: {list}')

import random
def mix_list(list):
    random.shuffle(list)
    print(f'Перемешанный список: {list}')
res = mix_list(list)
