name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Your data: ")
print("Your name" + name)
print("Your age: " + str(age))

if age < 8:
    print("Why did the cow cross the road?")
    print("To get to the moooovies")

elif age > 8 and age <= 12:
    print("Whats so great about Switzerland")
    print("Not sure though the flag is a big plus")
elif age > 12 and age <= 16:
    print("WHy can't you hear a pair of pteradactyl in the bathroom")
    print("Because it has a silent p.")
else:
    print("What has to be broken before you can use it?")
    print("An egg")