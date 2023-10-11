systemSettings = input("Is the system on (Y/N)?")
sens1 = input("Did alarm go off on the first floor(Y/N)? ")
sens2 = input("Did alarm go off on the second floor(Y/N)? ")

if systemSettings.lower() == "y":
    if sens1.lower() == "y":
        print("The alarm went off on the first floor.")
        if sens2.lower() == "y":
            print("The alarm went off on the second floor.")
        elif sens2.lower() == "n":
            print("Floor 2 is all clear")
        else:
            print("Invalid input.,")
    elif sens1.lower() == "n":
        print("Floor one is all clear.")
        if sens2.lower() == "y":
            print("The alarm went off on the second floor.")
        elif sens2.lower() == "n":
            print("Floor 2 is all clear.")
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
else:
    print("OK.")