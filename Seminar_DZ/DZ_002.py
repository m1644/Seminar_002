'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.    
    Пример:    
    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

'''
N = int(input('Введите число N: '))
f = 1
for i in range(N):
    i = i + 1
    f = i * f
    print(f, end = " ")
'''

def func(number):
    res = []
    t = 1
    for i in range(1, number + 1):
        t *= i
        res.append(t)
    print(res)

if __name__ == '__main__':
    chislo = int(input('Введите число N: '))
    func(chislo)
