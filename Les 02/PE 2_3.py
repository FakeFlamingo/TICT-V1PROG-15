age = int(input('Wat is je leeftijd?'))
pasport = input('Heb je een NL passport?')

if age >= 18 and pasport == 'ja' or pasport == 'Ja' or pasport == 'JA':
    print('Je mag stemmen!')
