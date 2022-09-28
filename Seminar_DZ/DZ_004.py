'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
'''

from random import randint

n = int(input('Введите число N: '))

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('4\n')

def get_numbers(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_mult(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

path = 'file.txt'
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print(numbers)
print(datalist)
print(get_mult(numbers, datalist))
