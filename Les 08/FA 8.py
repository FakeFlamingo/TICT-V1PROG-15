import xmltodict


def processXML(fileName):
    with open(fileName) as myXMLFile:
        fileContentString = myXMLFile.read()
        xmlDictionary = xmltodict.parse(fileContentString)
        return xmlDictionary


stationDict = processXML('stations.xml')

stations = stationDict['Stations']['Station']
print('Dit zijn de codes en types van de 4 stations:')
for station in stations:
    print('{:<7}{:<4}{}'.format(station['Code'], '-', station['Type']))

print()
print()
print('Dit zijn alle stations met één of meer synoniemen:')
for station in stations:
    if station['Synoniemen']:
        print('{:<7}{:<4}{}'.format(station['Code'], '-', station['Synoniemen']))

print()
print()
print('Dit is de lange naam van elk station:')
for station in stations:
    print('{:<7}{:<4}{}'.format(station['Code'], '-', station['Namen']['Lang']))
