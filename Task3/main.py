import random
number = random.randint(1, 1000000)
d = 2
while number % d != 0:
    d= d+1
print(f'Наименьшим натуральным делителем числа {number} является число {d}')