'''Q7. Average marks
Calculate and display the average marks of all students in the CSV file.'''
import csv
fo=open("csv1.csv",'r')
s=0
c=0
ro=csv.reader(fo)
next(ro)
for i in ro:
    s+=int(i[3])
    c+=1
print("Average Marks= ",(s)/c)
