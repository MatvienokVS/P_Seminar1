# Найдите сумму цифр трехзначного числа

number = input('Введите трехзначное число: ')

if len(number) == 3:
    print('Сумма чмсел трехзначного числа равна', end=' ')
    print(int(number[0]) + int(number[1]) + int(number[2]))
else:
    print('Вы ввели не трёхзначное число')
