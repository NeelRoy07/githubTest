ans = input("Is the car silent when you turn the key? (Yes/No) ")

if ans.lower() == "yes":
    ans = input("Are the battery terminals corroded")
    if ans.lower() == "yes":
        print("Clean the terminals and try starting again.")
    elif ans.lower() == "no":
        print("Replace cables and try again.")
    else:
        print("Please enter yes or no.")
elif ans.lower() == "no":
    ans = input("Does the car make a clicking noise? ")
    if ans.lower() == "yes":
        print("Replace the battery.")
    elif ans.lower() == "no":
        ans = input("Does the car crank up but fail to start? ")
        if ans.lower() == "no":
            print("Check spark plug connections. ")
        elif ans.lower() == "yes":
            ans = input("Does the engine start and then die? ")
            if ans.lower() == "no":
                print("Great! No urgent service required.")
            elif ans.lower() == "no":
                ans = int(input("How many seconds does your car stay on? "))
                if ans < 10:
                    print("Get it in for service.")
                elif ans > 10 and ans < 20:
                    print("Try again.")
                elif ans > 20:
                    ans = input("Does your car have fuel injection? ")
                    if ans.lower() == "yes":
                        print("Get it in for service")
                    elif ans.lower() == "no":
                        print("Check to ensure the choke is opening and closing.")
                    else:
                        print("Please enter yes or no.")
                else:
                    print("Please enter a number.")
            else:
                print("Please enter yes or no.")    
        else:
            print("Please enter yes or no.")
    else:
        print("Please enter yes or no.")
else:
    print("Please enter yes or no.")