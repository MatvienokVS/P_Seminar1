# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

max_value = int(input('Сколько всего поделок сделали дети: '))

value_Katy = max_value / 2
value_man = value_Katy / 2

name_string = None
if value_Katy == 1:
    name_string = 'поделку'
elif value_Katy >= 2 or value_Katy <= 4:
    name_string = 'поделки'
elif value_Katy >= 5:
    name_string = 'поделок'

print(f'Катя сделала {int(value_Katy)} {name_string}, Петя и Серёжа сделали по {int(value_man)} {name_string}')
