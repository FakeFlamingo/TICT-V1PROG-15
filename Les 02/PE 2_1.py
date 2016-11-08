money = eval(input('Wat verdien je per uur:'))
hours = eval(input('Hoeveel uur heb je gewerkt?'))

totalmoney = hours * money

print(str(hours) + ' uur werken levert ' + (str(totalmoney) + ' Euro op'))
