stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Den Bosch', 'Eindhoven',
            'Weert', 'Roermond', 'Sittard', 'Maastricht']

print('Welkom bij het traject Schagen - Maastricht')
# print('De volgende stations zijn beschikbaar:' + ','.join(stations))  # Niet perse nodig

beginStation = input('Van welk station vertrek je? ')
if beginStation not in stations:
    print('Dit station ligt niet in dit traject. Het begin station is ' + stations[0])
    beginStation = stations[0]

eindStation = input('Wat is je bestemming? ')
if eindStation not in stations or beginStation == eindStation:
    print('Dit is geen geldige bestemming. ' + stations[-1] + ' is gekozen')
    eindStation = stations[-1]

indexBeginStation = stations.index(beginStation)
indexEindStation = stations.index(eindStation)

if indexBeginStation > indexEindStation:
    print('Het gekozen eindstation ligt voor het startstation. Het einstation is nu veranderd naar ' + stations[-1])
    eindStation = stations[-1]
afstand = indexEindStation - indexBeginStation
prijs = 5
totalprijs = afstand * prijs

print('Het beginstation is ' + str(beginStation) + ' is het ' + str(indexBeginStation) + 'e station in het traject')
print('Het eindstation ' + str(eindStation) + ' is het ' + str(indexEindStation) + 'e station in het traject')
print('De afstand bedraagt ' + str(afstand) + ' station(s)')
print('De prijs van het kaartje is ' + str(totalprijs) + ' Euro')
print()
print('Jij stapt in de trein in: ' + str(beginStation))

for index in range(indexBeginStation + 1, indexEindStation):
    print('   - ' + stations[index])

print('Jij stapt uit in: ' + str(eindStation))
