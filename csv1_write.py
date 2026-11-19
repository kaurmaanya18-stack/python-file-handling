import csv
fo=open("csv1.csv","a+",newline="")
fo.seek(0)
for i in fo:
    print(i,end="")
wo=csv.writer(fo)
n=int(input("Enter no of inputs:"))
l=list()
for i in range(n):
    a=eval(input("Enter a list"))
    a=list(a)
    l.append(a)
wo.writerows(l)
fo.seek(0)
ro=csv.reader(fo)
for i in ro:
    print(i)
fo.seek(0)
for i in fo:
    print(i)
