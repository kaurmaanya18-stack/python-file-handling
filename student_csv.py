def csvread(fnm):
    fo=open(fnm,"r")
    s=0
    c=0
    for i in fo:
        a=i.strip().split(",")
        if(a[1].isdigit()):
            s+=int(a[1])
            c+=1
    if c>0:
        avg=s/c
    else:
        avg=0
    fo.close()
    return(f"{avg:.2f}")
print(csvread("student.csv"))
        

