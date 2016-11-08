infile = open('kaartnummers.txt', 'r')
content = infile.readlines()
infile.close()

print('Deze file telt: ' + str(len(content)) + ' regels.')

numbers = []
for x in content:
    a = int(x.split(',')[0])
    numbers.append(a)

maxNumber = (max(numbers))
regelMaxNumber = numbers.index(maxNumber) + 1
print('Het grootste kaartnummer is: ' + str(maxNumber) + ' en staat op regel ' + str(regelMaxNumber))
