'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
'''

from random import randint as rnd

number_ticket = str(rnd(100000, 1000000))

number_left = int(number_ticket[0]) + int(number_ticket[1]) + int(number_ticket[2])
number_right = int(number_ticket[3]) + int(number_ticket[4]) + int(number_ticket[5])

if number_left == number_right:
    print(f'Билет с номером {number_ticket} счастливый.')
else:
    print('Попробуйте проехать на другом автобусе.')

print(f'Попался билет с номером {number_ticket}')
print(f'Сумма первых трёх чисел равна {number_left}')
print(f'Сумма последних трёх чисел равна {number_right}')
