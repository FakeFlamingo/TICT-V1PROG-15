infile = open('kaartnummers.txt', 'r')
content = infile.readlines()
infile.close()

for x in content:
    x = x.split(',')
    print('{0} heeft kaartnummer: {1}'.format(x[1].rstrip(), x[0]))



