woord = ''

while True:
    woord = input('Geef een string van vier letters: ')

    lengte = len(woord)
    if lengte == 4:
        break
    else:
        print(woord + ' heeft ' + str(lengte) + ' letters ')

print('Inlezen van correcte string: ' + woord + ' is geslaagd')
