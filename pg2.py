fo=open("students.txt","r")
n=""
ct=0
ft=0
for i in fo:
    a=i.strip().split(",")
    ct+=1
    m=int(a[1])
    if m<60:
        n+=i.strip() +"\n"
        ft+=1
fo1=open("failed.txt","w")
fo1.writelines(n)
print("Total students: ",ct)
print("Failed students: ",ft)
fo.seek(0)
print("Students who passed:")
for i in fo:
    a=i.strip().split(",")
    m=int(a[1])
    if m>=60:
        print(a[0])
fo.close()
fo1.close()