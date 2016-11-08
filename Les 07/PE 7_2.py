import datetime
import csv

while True:
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y at %H:%M:%S").format('{} {} {} {}, {} {} {}')

    naam = input('Wat is je achternaam?     ')
    if naam == 'einde':
        break
    voorl = input('Wat zijn je voorletters?  ')
    gbdatum = input('Wat is je geboortedatum?  ')
    email = input('Wat is je e-mail adres?   ')

    with open('inloggers.csv', 'a', newline='', ) as myCSV:
        writer = csv.writer(myCSV, delimiter=';')

        writer.writerow((s, naam, voorl, gbdatum, email))

    myCSV.close()

print('Process gestopt!')
