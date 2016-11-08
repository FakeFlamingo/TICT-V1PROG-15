bedrijven = {
    'YAHOO': ['YHOO'],
    'GOOGLE INC': ['GOOG'],
    'Harley-Davidson': ['HOG'],
    'Yamana Gold': ['AUY'],
    "Sotheby's": ['BID'],
    'inBev': ['BUD']
}

def zoekTicker(bedrijfsnaam):
    print(bedrijven[bedrijfsnaam])


zoekTicker('inBev')


def zoekNaam(ticker):
    print(list(bedrijven.keys())[list(bedrijven.values()).index([ticker])])


zoekNaam('GOOG')


