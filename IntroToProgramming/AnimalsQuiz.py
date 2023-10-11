print("Welcome to our animal quiz!\n")
ans = input("Does it have fun (Yes/No: ")

if ans.lower() == "yes":
    print("It's a mamal!")
else:
    ans = input("Does it have feathers")
    if ans.lower() == "yes":
        print("It's a bird")
    else:
        ans = input("Does it have dry skin")
        if ans.lower() == "yes":
            print("It's a reptile")
        else:
            ans = input("Does it have scales?")
            if ans.lower() == "yes":
                print("It's a fish")
            else:
                print("It's an amphibian") 
