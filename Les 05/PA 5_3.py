invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = invoer.split('-')
lijst.sort()

newLijst = []
for x in lijst:
    newLijst.append(int(x))

print('Gesorteerde lijst van ints' + str(newLijst))
print('Grootste getal: ' + str(max(newLijst)) + ' en het kleinste getal: ' + str(min(newLijst)))
print('Aantal getallen: ' + str(len(newLijst)) + ' en de som van de getallen: ' + str(sum(newLijst)))
print('Gemiddelde: ' + str(sum(newLijst) / len(newLijst)))
