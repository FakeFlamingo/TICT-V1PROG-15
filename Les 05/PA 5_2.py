vraag = eval(input('Geef lijst met minimaal 10 strings: '))
aantal = len(vraag)

nieuwelijst = []
if aantal < 10:
    print('Helaas te weinig strings opgegegven!')
else:
    for i in vraag:
        lengt = len(i)
        if lengt == 4:
            nieuwelijst.append(i)

# print alleen de list als er iets instaat
if aantal < 10:
    ''
else:
    print(nieuwelijst)
