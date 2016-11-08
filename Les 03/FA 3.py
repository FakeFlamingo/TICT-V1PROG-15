# Activeer de bulk check
bulkCheck = True
leeftijd = ''
afstand = ''
weekend = ''

if not bulkCheck:
    leeftijd = int(input('Wat is je leeftijd? '))
    afstand = int(input('Wat is de afstand? In KM '))
    weekend = input('Is het weekend? Ja of Nee ')

if weekend == 'Ja' or weekend == 'ja' or weekend == 'JA':
    weekend = True
elif weekend == 'Nee' or weekend == 'nee' or weekend == 'NEE':
    weekend = False


def standaardprijs(afstandKM):
    if afstandKM < 50:
        x = afstandKM * 0.80
    if afstandKM >= 50:
        x = afstandKM * 0.60 + 15
    if afstandKM <= 0:
        x = afstandKM * 0
    return x


def ritprijs(leeftijd, weekendRit, afstandKM):
    x = standaardprijs(afstandKM)
    if leeftijd >= 12 < 65:
        if weekendRit:
            prijs = x * 0.60
        else:
            prijs = x
    elif leeftijd < 12:
        if weekendRit:
            prijs = x * 0.65
        else:
            prijs = x * 0.70

    elif leeftijd >= 65:
        if weekendRit:
            prijs = x * 0.65
        else:
            prijs = x * 0.70

    if bulkCheck:
        return round(prijs, 2)
    else:
        print(round(prijs, 2))


# leeftijd, weekendRit, afstandKM
if not bulkCheck:
    ritprijs(leeftijd, weekend, afstand)

# voor de bulk check
leeftijdCheck = [11, 12, 64, 65]
afstandCheck = [-15, 0, 5, 25, 50, 80]
weekendCheck = ()

if bulkCheck:
    for l in leeftijdCheck:
        for a in afstandCheck:
            print('leeftijd: ' + str(l) + ' Afstand: ' + str(a) + ' Weekend ' + str(ritprijs(l, True, a)) + ' euro')
            print('leeftijd: ' + str(l) + ' Afstand: ' + str(a) + ' Doordeweeks ' + str(ritprijs(l, False, a)) + ' euro')
            print()
        print('----------------------------------------------------------')
