'''fo=open("csv1.csv","r")
for i in fo:
    for j in i:
        print(j)'''
import csv
fo=open("csv1.csv","r")
ro=csv.reader(fo)
for i in ro:
    print (i)