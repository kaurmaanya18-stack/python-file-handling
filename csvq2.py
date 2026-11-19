'''Q2. Marks-based searching
Display the names and marks of students who scored more than 80.'''
import csv
fo=open("csv1.csv","r")
ro=csv.reader(fo)
next(ro)
for i in ro:
    if int(i[3])>=80:
        print("Name:",i[0],end=" ")
        print("Marks:",i[3])
