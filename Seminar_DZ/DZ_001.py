'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.    
    Пример:    
    - 6782 -> 23
    - 0,56 -> 11
'''

'''
num = input('Введите вещественное число: ')
sum = 0
for i in num:
    if i != ".":
        sum = sum + int(i)
print(f'Сумма цифр числа {num} равна =', sum)
'''

def func(number):
    sum = 0
    for symbol in number:
        if symbol != '.':
            sum += int(symbol)
    return sum

if __name__ == '__main__':
    chislo = input('Введите вещественное число: ')
    summary = func(chislo)
    print(f'Сумма цифр числа {chislo} равна =', summary)
