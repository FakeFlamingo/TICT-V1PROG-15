klas = {}

invoer = input('Vul uw naam in: ')

while invoer is not '':
    if invoer not in klas:
        klas[invoer] = 1
    else:
        klas[invoer] += 1
    invoer = input('Vul uw naam in: ')


for (key,value) in klas.items():
            if value == 1:
                print('Er is '+ str(value) +' student met de naam ' + str(key))
            else:
                print('Er zijn '+ str(value) +' studenten met de naam ' + str(key))
