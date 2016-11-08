tabel = [0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 23]
aantalrijen = len(tabel)
aantalkollomen = len(tabel[0])
aantalpixels = 0

for i in range(aantalrijen):
    for j in range(aantalkollomen):
        if tabel[i][j] > 0:
            aantalpixels += 1

print(aantalpixels)
