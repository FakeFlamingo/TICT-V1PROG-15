def kwadratenSom(grondgetallen):
    res = 0
    for i in range(len(grondgetallen)):
        if grondgetallen[i] > 0:
            res = res + grondgetallen[i] ** 2
    return res


grondgetallen = [4, 5, 3, -81]

print(kwadratenSom(grondgetallen))
