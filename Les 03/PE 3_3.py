def langGenoeg(Centimeter):
    if Centimeter >= 120:
        res = 'Je bent lang genoeg voor de attractie!'
    else:
        res = 'Sorry, je bent te klein!'

    print(res)


Centimeter = int(input('Hoe lang ben je? '))
res = langGenoeg(Centimeter)
