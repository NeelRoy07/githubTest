gr = input("Would you like to enter grade (Y/N): ")
y = 0
x = 0

while gr.lower() == "y":
    grade = int(input("Enter a grade: "))

    x = x + 1
    y = y + grade

    gr = input("Would you like to enter another grade (Y/N): ")

print("You average is ", (y/x))
