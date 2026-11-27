def write(fnm,md):
    fo=open(fnm,md)
    while True:
        a=input()+"\n"
        if a==(""+"\n"):
            break
        else:
            fo.write(a)
    fo.close()
def read(fnm):
    fo=open(fnm,"r")
    w=fo.readlines()
    for i in w:
        print(i,end="")
    return(w)
#write("students.txt","a+")
a=read("students.txt")
s=0
c=0
for i in a:
    l=i.strip().split(",")
    s+=int(l[1])
    c+=1
avg=s/c
print("Average: ",avg)
