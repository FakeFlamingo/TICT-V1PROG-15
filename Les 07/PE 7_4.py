import csv

with open('voorraad.csv', 'r', newline='', ) as myCSV:
    reader = csv.reader(myCSV, delimiter=';')
    next(reader)
    highestPrice = 0.00
    highestPriceName = ''
    lowestStocknumer = 999999999
    lowestStockName = ''
    totalItemCount = 0

    for row in reader:

        if float(row[4]) > highestPrice:
            highestPrice = float(row[4])
            highestPriceName = row[2]

    myCSV.seek(0)
    next(reader)
    for row in reader:

        if int(row[3]) < lowestStocknumer:
            lowestStocknumer = int(row[3])
            lowestStockName = row[0]

    myCSV.seek(0)
    next(reader)
    for row in reader:
        totalItemCount += int(row[3])

print('Het duurste artikel is ' + highestPriceName + ' en die kost ' + str(highestPrice))
print('Er zijn slechts ' + str(
    lowestStocknumer) + ' exemplaren in voorraad can het product met nummer ' + lowestStockName)
print('In totaal hebben wij ' + str(totalItemCount) + ' producten in ons magazijn liggen')
