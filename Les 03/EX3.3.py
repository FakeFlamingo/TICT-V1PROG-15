lst = [4, 0, 1, -2]


def wissel(lst):
    lst[0], lst[1] = lst[1], lst[0]
    return lst


x = wissel(lst)
print(x)
