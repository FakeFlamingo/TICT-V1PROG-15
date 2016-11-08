import random


def monopolyworp():
    res1 = random.randrange(1, 7)
    res2 = random.randrange(1, 7)

    print(res1, '+', res2, '=', (res1 + res2))

    if res1 == res2:
        print('Eerste worp was gelijk je mag voor de 2e keer gooien!!!')
        res3 = random.randrange(1, 7)
        res4 = random.randrange(1, 7)
        print(res3, '+', res4, '=', (res3 + res4))

        if res3 == res4:
            print('Tweede worp was gelijk!! Gooi niet nog een keer gelijk!!')
            res5 = random.randrange(1, 7)
            res6 = random.randrange(1, 7)
            print(res5, '+', res6, '=', (res5 + res6))
            if res5 == res6:
                print('Je hebt drie keer gelijk gegooit je moet naar de gevangenis!')
    print('------------------')


for i in range(1, 5000):
    monopolyworp()
