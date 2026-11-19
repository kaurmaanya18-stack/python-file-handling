'''Q8. Count students course-wise
Count how many students belong to each course.'''
import csv

fo = open("csv1.csv", "r")
ro = csv.reader(fo)
next(ro)

c = []
a = []
c1 = 0

for i in ro:
    if i[2] not in a:
        a.append(i[2])

for i in a:
    fo.seek(0)
    r1 = csv.reader(fo)
    next(r1)
    c1 = 0

    for j in r1:
        if i == j[2]:
            c1 += 1

    print("Course:", i, "Frequency:", c1)


