fo=open("students.txt","r+")
nm=input("Enter student name: ")
um=input("Enter updated marks: ")
k=0
for i in fo:
    a=i.strip().split(",")
    if a[0]==nm:
        k+=1
new=""
if k>0:
    fo.seek(0)
    for i in fo:
        a=i.strip().split(",")
        if a[0]==nm:
            new+=a[0]+","+um+"\n"
        else:
            new+=i
    fo.seek(0)
    fo.truncate(0)
    fo.writelines(new)
else:
    print("Student not found")


