"""Als extra beveiliging wil de NS op haar E-ticket nog een unieke code afbeelden. Er is gekozen voor een
hele eenvoudige beveiliging: Neem de naam van de gebruiker+beginstation+eindstation, vertaal elk
karakter naar ASCII en maak die waarde 3 groter. De “a” wordt dus een “d”, de “b” wordt een “e”, etc.
De “A” wordt een “D”, de “W” wordt een “Z”, etc. En de spatie “ ” wordt een “#” .

Zorg ervoor dat je code maakt die deze uitvoer maakt op basis van de invoer van de gebruiker. Schrijf
een functie: def code(invoerstring): die ieder teken van invoerstring omzet naar zijn
rangordenummer met bibliotheekfunctie ord(), en – na er 3 bij te hebben opgeteld – die int-waarde
weer terug vertaalt naar het bijbehorende ASCII-teken met bibliotheekfunctie chr()."""

naam = input('Wat is je naam?')
instapStation = input('In welk station stap je in?')
uitstapStation = input('Waar stapt uw uit?')

vragen = naam + instapStation + uitstapStation

letters = []


def code(invoerstring):
    for i in invoerstring:
        new = ord(i) + 3
        letters.append(new)

    for i in letters:
        coded = chr(i)
        print(coded, end='')


code(vragen)
