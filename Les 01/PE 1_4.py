cijferICOR = 5.5
cijferPROG = 7.1
cijferCSN = 9.2

gemiddeld = (cijferCSN + cijferICOR + cijferPROG) / 3

beloning = 30

money = gemiddeld * beloning

overzicht = 'Mijn cijfers (Gemiddeld een ' + str(gemiddeld) + ')' + 'leveren een beloning op van €' + str(
    money) + ' op!'

print(overzicht)
