fileGeannuleerd = open('geannuleerd.txt', 'r')
geannuleerd = fileGeannuleerd.readlines()
fileGeannuleerd.close()

fileTreinRitten = open('treinritten.txt', 'r')
treinritten = fileTreinRitten.readlines()
fileTreinRitten.close()

cleanGeannuleerd = []
for i in geannuleerd:
    mutatie = i.split(': ')
    cleanGeannuleerd.append(mutatie[1])

final = open('final.txt', 'a')
for regel in treinritten:
    treinrit = regel.split(' - ')
    bestemming = treinrit[1]
    if bestemming not in cleanGeannuleerd:
        final.write(regel)

final.close()
