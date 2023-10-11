password = "abc123"

count = 1

while True:
    userpw = input("Please enter the password: ")
    if userpw == password:
        print("Welcome")
        break

    elif count > 3:
        print("You have entered the wrong password too many times.")
        break
    
    else:
        print("Try again.")
        count = count + 1