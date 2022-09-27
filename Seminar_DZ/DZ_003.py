'''
3. Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму 
(округляйте до 3 знаков после запятой).    
    Пример:    
    - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
'''

n = int(input('Введите количество чисел в списке: '))

def numbers(n):
    summ = 0
    for i in range(n):
        a = int(input(f'Введите число {i + 1}: '))
        a = (1 + 1/a) ** a
        summ = a + summ
        i += 1
    return summ

print('Сумма чисел равна =', round((numbers(n)), 3))