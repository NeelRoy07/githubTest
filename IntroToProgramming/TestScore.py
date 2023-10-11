t1 = int(input("Enter your test score: "))
t2 = int(input("Enter your test score: "))
t3 = int(input("Enter your test score: "))

average = round((t1 + t2 + t3) / 3,2)

if average > 95:
    print("Great job for getting " + str(average))
elif average <= 95 and average >= 80:
    print("Good job for getting " + str(average))
else:
    print("Good try! You got " + str(average))

