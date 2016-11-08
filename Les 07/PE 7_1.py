def calc():
    # noinspection PyBroadException

    try:
        euro = int(input('Hoeveel euro?'))
        personen = int(input('Hoeveel personen?'))

        if euro < 0:
            print('Negatieve getallen zijn niet toegestaan!')
        elif personen < 0:
            print('Negatieve getallen zijn niet toegestaan!')
        else:
            cost = float(euro) / int(personen)
            print(cost, str('euro per persoon'))

    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except:
        print('Onjuiste invoer!')


calc()
