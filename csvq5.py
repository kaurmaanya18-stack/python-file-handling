'''Q5. Maximum marks
Find and display the complete record of the student who scored the highest marks.'''
import csv
fo=open("csv1.csv","r")
marks=list()
ro=csv.reader(fo)
next(ro)
for i in ro:
    marks.append(int(i[3]))
mm=max(marks)
fo.seek(0)
ro=csv.reader(fo)
next(ro)
for i in ro:
    if int(i[3])==mm:
        for j in i:
            print(j,end=" ")