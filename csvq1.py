'''Q1. Basic searching
Write a program to display all records of students whose course is Q1. Basic searching
Write a program to display all records of students whose course is BCA AI ML'''
fo=open("csv1.csv","r")
for i in fo:
    if "BCA AI ML" in i:
        print(i,end="")
    else:
        continue