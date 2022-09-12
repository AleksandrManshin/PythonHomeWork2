from random import randint
odnoklassniki_growth =[]
for i in range(8):
    odnoklassniki_growth.append(randint(150, 200))
odnoklassniki_growth.sort(reverse = True)
print (f'Рост 8-ми учеников в порядке убывания: {odnoklassniki_growth}')
petya_growth = int(input('Введите рост Пети: '))
odnoklassniki_growth.append(petya_growth)
odnoklassniki_growth.sort(reverse = True)
print(f'Место Пети в шеренге: {odnoklassniki_growth.index(petya_growth)+1}')