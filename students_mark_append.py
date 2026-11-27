def update_csv(fnm,nm,mks):
    fo=open(fnm,"r+")
    n=""
    l=list()
    for i in fo:
        a=i.strip().split(",")
        if(a[1]==nm):
            n=a[0]+","+a[1]+","+str(mks)+"\n"
        else:
            n=i.strip()+"\n"
        l.append(n)
        n=""
    fo.seek(0)
    fo.writelines(l)
    fo.truncate()
    fo.close()
update_csv("students_mark.csv","Harmanpreet",100)



