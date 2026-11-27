def stmcsvread(fnm):
    fo=open(fnm,"r")
    fo1=open("passed.csv","w")
    n=""
    l=list()
    for i in fo:
        a=i.strip().split(",")
        if a[2].isdigit():
            if int(a[2])>=60:
                n+=i.strip()+"\n"
        else:
            n+=i.strip()+"\n"
        l.append(n)
        n=""
    fo1.writelines(l)
    fo.close()
    fo1.close()
stmcsvread("students_mark.csv")
