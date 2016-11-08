zin = input('Voer een zin in')

woorden = zin.split()
res = ''

for woord in woorden:
    res += woord[0].upper()

print(res)
