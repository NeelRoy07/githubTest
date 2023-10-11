grd = int(input("What is your grade? "))
att = int(input("What is your attendance percentage throughout the year? "))

if att > 90:
    if grd > 90:
        print("Your grade is an A.")
    elif grd <= 90 and grd > 80:
        print("Your grade is a B.")
    elif grd <= 80 and grd > 70:
        print("Your grade is a C.")
    else:
        print("You fail.")

else:
    print("You fail.")