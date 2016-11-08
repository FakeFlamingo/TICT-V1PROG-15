import csv

with open('gameHighScores.csv', 'r', newline='', ) as myCSV:
    reader = csv.reader(myCSV, delimiter=';')

    lijst = []
    for row in reader:
        lijst.append(row[2])
        highest = max(lijst)

    myCSV.seek(0)

    for row in reader:
        if row[2] == highest:
            print('De hoogste score is: ' + highest + ' op ' + row[1] + ' behaald door ' + row[0])





