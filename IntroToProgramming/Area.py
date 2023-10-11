import math

drinks_no = int(input("How many drinks have they consumed? "))
body_weight = int(input("How much does the person weigh in pounds? "))
hours_since_drink = int(input("How many hours has it been since their last drink?"))
gender = input("What is the gender of this person? ")
com = input("Are you a commercial driver? ")
age = int(input("How old are you? "))


if gender.lower == "man":
    r = 0.68
else:
    r = 0.55

bac = round((drinks_no * 14) / (body_weight * 4.54 * r) - (0.015 * hours_since_drink), 3)

if com.lower() == "yes":
    if bac > 0.04:
        print("The person's blood alcohol level is: " + str(bac) + ", this person cannot legally drive.")
    else:
        print("This person's blood alcohol level is: " + str(bac) + " can legally drive.")
elif age >= 21:
    if bac > 0.08:
        print("The person's blood alcohol level is: " + str(bac) + ", this person cannot legally drive.")
    else:
        print("This person's blood alcohol level is: " + str(bac) + " can legally drive.")
else:
    if bac > 0.02:
        print("This person's blood alcohol is: " + str(bac) + ", this person cannot legally drive")
    else:
        print("This person's blood alcohol is: " + str(bac) + " can legally drive." )