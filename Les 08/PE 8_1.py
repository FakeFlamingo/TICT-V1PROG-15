import xmltodict


def processXML(fileName):
    with open(fileName) as myXMLFile:
        fileContentString = myXMLFile.read()
        xmlDictionary = xmltodict.parse(fileContentString)
        return xmlDictionary


productDict = processXML('bestand.xml')

products = productDict['artikelen']['artikel']
print('Naam | Prijs | Voorraad')
for product in products:
    print(product['naam'], '|', product['prijs'], '|', product['voorraad'])
