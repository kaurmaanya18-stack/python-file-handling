'''Q6. Minimum marks
Find and display the name of the student who scored the lowest marks.'''
import csv
fo=open("csv1.csv","r")
ro=csv.reader(fo)
m=list()
next(ro)
for i in ro:
    m.append(int(i[3]))
lm=min(m)
ro=csv.reader(fo)
fo.seek(0)
next(ro)
for i in ro:
    if int(i[3])==lm:
        for j in i:
            print(j,end=" ")