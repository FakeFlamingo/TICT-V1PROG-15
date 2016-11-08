def convert(gradenCelsius):
    fahrenheit = gradenCelsius * 1.8 + 32
    return fahrenheit


def table():
    print('{:>3} {:>9}'.format('F', 'C'))
    for x in range(-30, 41, 10):
        f = convert(x)
        print('{:<7.1f}{:>8.1f}'.format(f, x))


table()
