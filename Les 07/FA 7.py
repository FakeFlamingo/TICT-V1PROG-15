import csv
import random


def aantalKluizenVrij():
    aantal = 0
    with open('kluizen.csv', 'r', newline='', ) as myCSV:
        reader = csv.reader(myCSV, delimiter=';')
        for row in reader:
            if row[1] == 'vrij':
                aantal += 1
    return 'Er zijn nog ' + str(aantal) + ' kluizen vrij'


def nieuweKluis():
    with open('kluizen.csv', 'r', newline='', ) as myCSV:
        reader = csv.reader(myCSV, delimiter=';')
        next(reader)
        lijst = []
        for row in reader:
            lijst.append(row)
    for i in lijst:
        if i[1] == 'vrij':
            pincode = random.randrange(1000, 9999)
            i[1] = 'bezet'
            i[2] = pincode
            print('De pincode is ' + str(pincode))
            print('De kluis is nummer: ' + i[0])
            print('Deze pincode AUB onthouden!')
            break

    with open('kluizen.csv', 'w', newline='', ) as myCSVWrite:
        writer = csv.writer(myCSVWrite, delimiter=';')

        writer.writerow(('kluisnummer', 'beschikbaarheid', 'code'))

        for i in lijst:
            writer.writerow((i[0], i[1], i[2]))


def kluisOpenen():
    with open('kluizen.csv', 'r', newline='', ) as myCSV:
        reader = csv.reader(myCSV, delimiter=';')
        next(reader)
        lijst = []
        for row in reader:
            lijst.append(row)

    pinCode = input('Geef de pincode op: ')
    for i in lijst:

        if str(i[2]) == str(pinCode):
            print('Kluis ' + str(i[0]) + ' geopend!')
            break


def kluisTerugGeven():
    with open('kluizen.csv', 'r', newline='', ) as myCSV:
        reader = csv.reader(myCSV, delimiter=';')
        next(reader)
        lijst = []
        for row in reader:
            lijst.append(row)

    pincode = input('Voer uw pincode in: ')

    for i in lijst:
        if str(i[2]) == str(pincode):
            i[1] = 'vrij'
            with open('kluizen.csv', 'w', newline='', ) as myCSVWrite:
                writer = csv.writer(myCSVWrite, delimiter=';')

                writer.writerow(('kluisnummer', 'beschikbaarheid', 'code'))

                for x in lijst:
                    writer.writerow((x[0], x[1], x[2]))


def geefAlleKluizenVrij():
    with open('kluizen.csv', 'r', newline='', ) as myCSV:
        reader = csv.reader(myCSV, delimiter=';')
        next(reader)
        lijst = []
        for row in reader:
            lijst.append(row)
    pincode = input('Vul de geheime code in')

    if pincode == 'wachtwoord':
        for i in lijst:
            i[1] = 'vrij'
        with open('kluizen.csv', 'w', newline='', ) as myCSVWrite:
            writer = csv.writer(myCSVWrite, delimiter=';')

            writer.writerow(('kluisnummer', 'beschikbaarheid', 'code'))

            for x in lijst:
                writer.writerow((x[0], x[1], x[2]))


while True:

    print('1: Ik wil een nieuwe kluis')
    print('2: Ik wil mijn kluis openen')
    print('3: Ik geef mijn kluis terug')
    print('4: Ik wil weten hoeveel kluizen nog vrij zijn')
    nummer = input('Vul een nummer in: ')

    if nummer == str(1):
        nieuweKluis()
    elif nummer == str(2):
        kluisOpenen()
    elif nummer == str(3):
        kluisTerugGeven()
    elif nummer == str(4):
        print(aantalKluizenVrij())
    elif nummer == str(5):
        break
    elif nummer == str(6):
        geefAlleKluizenVrij()
