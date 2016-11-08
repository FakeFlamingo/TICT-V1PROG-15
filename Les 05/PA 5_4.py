total = 0
lijst = []
while True:
    number = int(input('Geef een getal'))

    if number == 0:
        break
    else:
        total += number
        lijst.append(number)

print('Er zijn ', str(len(lijst)) + ' getallen ingevoerd' + ' en de som is: ' + str(total))
