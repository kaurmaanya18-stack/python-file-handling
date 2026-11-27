
def read(fnm):
    try:
        fo = open(fnm, "r")

        highest = 0
        c = 0
        marks = 0

        for i in fo:
            a = i.strip().split(",")
            name = a[0]
            mark = int(a[1])

            c += 1
            marks += mark

            if highest <= mark:
                highest = mark
                topper = name

        if c == 0:
            print("File is empty")
            fo.close()
            return

        avg = marks / c

        print("Total students:", c)
        print("Topper:", topper)
        print(f"Average marks: {avg:.2f}")

        print("Students scoring above average:")

        fo.seek(0)

        for i in fo:
            a = i.strip().split(",")
            if int(a[1]) > avg:
                print(a[0])

        fo.close()

    except FileNotFoundError:
        print("File not found")

read("students.txt")
