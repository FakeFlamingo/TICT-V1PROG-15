bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

# set-functie welke plaatsen in beide trajecten worden aangedaan (de overeenkomst).
print(bruin & groen)

"""Gebruik vervolgens opnieuw een set-functie om te printen
hoe het traject “bruin” verschilt van het traject “groen”. Je
moet dan dus op het scherm zien welke plaatsen van
traject “bruin” ze niet allebei aandoen!"""

print(bruin ^ groen)








# #Print ook alle stations op beide trajecten uit. Print elk station maar 1! Gebruik weer een set-functie!
print(bruin | groen)
