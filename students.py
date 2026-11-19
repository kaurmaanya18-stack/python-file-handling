fo=open("student.txt","w")
l=list()
for i in range(5):
    l.append(input("Enter Student name:")+"\n")
fo.writelines(l)
fo.close()