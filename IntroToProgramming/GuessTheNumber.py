import random

num = random.randint(1,100)
ans = int(input("Guess a number between 1 and 100: "))
count = 1

while num != ans:
    if ans > num:
        print("To high")
    elif ans < num:
        print("To low")
    ans = int(input("Guess a number between 1 and 100: "))
    count += 1

print("You are correct. It took you", count, "tries to get the answer.")