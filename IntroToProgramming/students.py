students1 = 0
students2 = 0

def getStudentsP3():
    global students1
    students1 = int(input("How many students are in p3: "))

def getStudentsP5():
    global students2
    students2 = int(input("How many students are in p5: "))

getStudentsP3()
getStudentsP5()
print("The total number of students is", (students1 + students2))