fo=open("student.txt","r")
try:
    l=fo.readlines()
    for i in l:
        print(i,end="\n")
except EOFError:
    print("End of file reached")