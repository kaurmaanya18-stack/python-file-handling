'''Q3. City-based searching
Display all records of students belonging to Delhi.'''
import csv
fo=open("csv1.csv","r")
ro=csv.reader(fo)
for i in ro:
    if i[4]=="Delhi":
        for j in i:
            print(j,end=" ")
        print()
