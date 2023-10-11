Temp = float(input("What is your temperature in degrees centigrade? "))

if temp > 37.2:
    sore = input("Is your throat soar (Y/N)? ")
    if sore.lower() == "y":
        print("You have a thraot infection.")
    elif sore.lower() == "n":
        cough = input("Do you have a cough (Y/N)? ")
        if cough.lower() == "y":
            print("You have a chest infection.")
        elif cough.lower() == "n":
            print("You have a fever.")
        else:
            print("Invalid input.")
    else:
        print("invalid input.")

elif temp < 36.1:
    sore = input("Is your throat soar (Y/N)? ")
    if sore.lower() == "y":
        print("You have a thraot infection.")
    elif sore.lower() == "n":
        cough = input("Do you have a cough (Y/N)? ")
        if cough.lower() == "y":
            print("You have a chest infection.")
        elif cough.lower() == "n":
            print("You have a fever.")
        else:
            print("Invalid input.")
    else:
        print("invalid input.")

elif temp < 37.2 and temp > 36.1:
    print("You are in perfect health.")

else: 
    print("Invalid input.")