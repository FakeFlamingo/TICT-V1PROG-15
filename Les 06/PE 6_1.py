
students = {
    'Paul Jansen': [5, 5, 3, 2, 2, 7, 4],
    'Jan Jansen': [2, 3, 5, 8, 3, 2, 10, 22],
    'Frank Jansen': [15, 44, 33, 21, 4, 2]
            }

for person in students:
    for number in students[person]:
        if number >= 10:
            print(person + ' ' + str(number))

