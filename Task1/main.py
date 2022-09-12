import random

quantity = int(input('Введите кол-во монет: '))
count = 0

for i in range(quantity):
    side = random.randint(0, 1)
    print(side, end='\n')
    if side == 0:
        count = count + 1
print(f"Кол-во монет перевернутых гербом вверх: {count}")
