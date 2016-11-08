import datetime

vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S,").format('{} {} {} {}, {} {} {}')

dagInNumber = 20
dagInText = 'Di'
maandInText = 'Mar'
maandInNumber = 9
year = 2016

# uur = int(input('Wat is het uur? '))
# minuut = int(input('Minuut? '))
# seconde = int(input('Seconde? '))
naam = str(input('Wat is de naam van de hardloper?'))

# total = '{0} {1} {2} {3}, {4}:{5}:{6}, {7}'.format(dagInText, str(dagInNumber), maandInText, str(year), str(uur),
#                                                   str(minuut), str(seconde), naam)

total = s + ' ' + naam

file = open('hardlopers.txt', 'a')

file.write("{}\n".format(total))

file.close()
