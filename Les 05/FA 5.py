stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Den Bosch', 'Eindhoven',
            'Weert', 'Roermond', 'Sittard', 'Maastricht']


def inlezenBeginpunt(begin):
    beginStation = begin

    while beginStation not in stations:
        beginStation = input('Van welk station vertrek je? ')
        if beginStation not in stations:
            print('Station ' + beginStation + 'ligt niet in dit traject.')
    return beginStation


def inlezenEindpunt(begin, eind):
    beginStation = inlezenBeginpunt(begin)
    eindStation = eind
    while eindStation not in stations or stations.index(begin) >= stations.index(eindStation):

        if beginStation == eindStation:
            print('Het begin en eindstation kunnen niet het zelfde zijn')
        else:
            print('Station ' + eindStation + ' is ongeldig!')
        eindStation = input('Kies een nieuwe bestemming ')

    return eindStation


def omroepenReis(begin, eind):
    print('Welkom bij het traject Schagen - Maastricht')
    beginStation = inlezenBeginpunt(begin)
    eindStation = inlezenEindpunt(beginStation, eind)

    indexBeginStation = stations.index(beginStation)
    indexEindStation = stations.index(eindStation)

    afstand = indexEindStation - indexBeginStation
    prijs = 5
    totalprijs = afstand * prijs

    print('Het beginstation is ' + str(beginStation) + ' is het ' + str(
        indexBeginStation + 1) + 'e station in het traject')
    print('Het eindstation ' + str(eindStation) + ' is het ' + str(indexEindStation + 1) + 'e station in het traject')
    print('De afstand bedraagt ' + str(afstand) + ' station(s)')
    print('De prijs van het kaartje is ' + str(totalprijs) + ' Euro')
    print()
    print('Jij stapt in de trein in: ' + str(beginStation))

    for index in range(indexBeginStation + 1, indexEindStation):
        print('   - ' + stations[index])

    print('Jij stapt uit in: ' + str(eindStation))


omroepenReis('Alkmaar', 'Weert')
