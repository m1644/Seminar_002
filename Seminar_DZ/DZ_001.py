'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.    
    Пример:    
    - 6782 -> 23
    - 0,56 -> 11
'''

num = input('Введите вещественное число: ')
sum = 0
for i in num:
    if i != ".":
        sum = sum + int(i)
print(f'Сумма цифр числа {num} равна =', sum)
