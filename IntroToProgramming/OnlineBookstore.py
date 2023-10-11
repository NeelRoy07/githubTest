cost = int(input("What is the total cost of your order? "))
sig = input("Would you like to pay signature (Y/N)? ")

if sig.lower() == "y":
    Total = cost + 5
    if Total >= 15:
        print("Your overall cost is £", Total, ".")
    elif Total <= 15:
        Total = Total + 3.5
        print("Your overall cost is £", Total, ".")
    else:
        print("You must enter Y or N.")
elif sig.lower() == "n":
    if cost >= 15:
        print("Your overall cost is £", cost, ".")
    elif cost <= 15:
        Total = cost + 3.5
        print("Your overall cost is £", Total, ".")
    else:
        print("You must enter Y or N.")
else:
    print("You have entered something invalid. Try again.")