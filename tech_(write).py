fo=open("tech.txt","w+")
fo.write("Technology has transformed the way people learn, communicate, and work.\nEvery day, millions of students use digital platforms to access educational resources, submit assignments, and collaborate with others.\nHowever, technology also requires responsible usage because excessive screen time and distractions can affect productivity.\nDeveloping good habits, managing time effectively, and continuously learning new skills are essential for personal and professional growth.\nThe future belongs to individuals who can combine creativity, critical thinking, and technical knowledge to solve real-world problems.")
fo1=open("techCopy.txt","w")
fo.seek(0)
l=fo.readlines()
fo1.writelines(l)
lines=1
chars=0
alphas=0
nos=0
words=0
for i in l:
    words+=len(i.split())
    for j in i:
        if j.isalpha():
            alphas+=1
        elif j.isdigit():
            nos+=1
        chars+=1
        if j=="\n":
            lines+=1
print("Alphabets:",alphas)
print("Numbers:",nos)
print("Characters:",chars)
print("Lines:",lines)
print("Words:",words)