'''Q9: Display students scoring above the average'''
import csv

fo = open("csv1.csv", 'r')
s = 0
c = 0

ro = csv.reader(fo)
next(ro)

for i in ro:
    s += int(i[3])
    c += 1

avg1 = s/c
print("Average Marks =", avg1)

fo.seek(0)
ro = csv.reader(fo)
next(ro)

print("Students whose marks are greater than average are:")

for i in ro:
    if int(i[3]) > avg1:
        print(i[0])

fo.close()