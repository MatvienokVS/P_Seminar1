'''
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
'''

horizont_value = int(input('Введите количество долек по горизонтале: '))
vertical_value = int(input('Введите количество долек по горизонтале: '))
breake_value = int(input('Введите количество долек по горизонтале: '))

if (breake_value % horizont_value) == 0 or (breake_value % vertical_value) == 0:
    print('yes')
else:
    print('No')
