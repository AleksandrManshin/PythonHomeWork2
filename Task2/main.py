numb = int(input('Введите количество чисел, которое нужно сложить от 1 до N: '))
n = 0
for i in range(numb + 1):
    n = n + i
print (f'Cумма чисел равна: {n} ')