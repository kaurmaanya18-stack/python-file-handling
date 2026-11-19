'''Count the number of students whose age is 19.'''
import csv
fo=open("csv1.csv","r")
c=0
ro=csv.reader(fo)
for i in ro:
    if i[1]=='19':
        c+=1
print("No. of 19 year olds:",c)