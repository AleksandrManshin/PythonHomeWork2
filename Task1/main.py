import random

quantity = int(input('Введите кол-во монет: '))
count = 0
count2 = 0

for i in range(quantity):
    side = random.randint(0, 1)
    print(side, end='\n')
    if side == 0:
        count = count + 1
    else:
        count2 = count2 + 1
if count < count2:
    print(f"Кол-во монет которые нужно перевернуть решкой вверх: {count}")
else:
    print(f"Кол-во монет которые нужно перевернуть гербом вверх: {count2}") 
