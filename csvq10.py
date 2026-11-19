''''Q10. Update a student's marks
Write a Python program to change Maanya's marks from 95 to 99 in csv1.csv'''
import csv
fo=open("csv1.csv","r",newline="")
ro=csv.reader(fo)
l=list()
a=list()
for i in ro:
    for j in range(4):
        if j==3:
            if "Mehak" in i[0]:
                a.append('45'.strip())
            else:
                a.append(i[j].strip())
        else:
            a.append(i[j].strip())
    l.append(a)
    a=[]
fo.close()
fo=open("csv1.csv","w",newline="")
wo=csv.writer(fo)
wo.writerows(l)
fo.close()