studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddeldePerStudent(studentenCijfers):
    gem = []
    for student in studentenCijfers:
        gem.append(float(sum(student)) / max(len(student), 1))

    return gem


def gemiddeldeVanAlleStudenten(studentenCijfers):
    perStudent = gemiddeldePerStudent(studentenCijfers)
    return float(sum(perStudent)) / max(len(perStudent), 1)


print(gemiddeldePerStudent(studentencijfers))
print(gemiddeldeVanAlleStudenten(studentencijfers))
