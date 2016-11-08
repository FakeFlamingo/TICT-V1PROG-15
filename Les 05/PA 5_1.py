def seizoen(maand):
    if maand == 3 or maand == 4 or maand == 5:
        print('Lente')
    elif maand == 6 or maand == 7 or maand == 8:
        print('Zomer')
    elif maand == 9 or maand == 10 or maand == 11:
        print('Herfst')
    elif maand == 12 or maand == 1 or maand == 2:
        print('Winter')
    else:
        print('Ongeldige ingave')

vraag = int(input('Vul het getal van de maand in: '))

seizoen(vraag)
