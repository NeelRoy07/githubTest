"""
Description: This program is an adventure game that has two locations. Either you go to the castle or the forest and your main objective is to save the prince.
Name: Neel Roy
Date: 04/03/22
Period: 8
"""
import random #imports the random library

#Introduction
name = input("Enter your name: ")
print("Welcome, " + name + ", to the final level of “Medieval Quest”.")
print("\nAfter a long adventure, " + name + "’s map has indicated that he is at his final destination. He has encountered a fork in his path, at which the signs read “Forest” or “Castle”. Help " + name + " reach the prince.")
print()
ans = int(input("Type 1 for Forest, and 2 for Castle. "))

#takes you to the forest for that part of the game
if ans == 1:
    print("Welcome to the Forest! The Dark Elf name Aivil Otolip is here to decide your destiny. However, she feels the only way to know who wins or loses, is a roll of the dice. If the Dark Elf gets a higher number (1-10) than you (1-10), the Dark Elf wins; a lower number and the Dark Elf loses; the same number and she becomes friends with you.")
    rand1 = random.randint(1,10)
    rand2 = random.randint(1,10)

    print("Aivil has rolled a " + str(rand1))
    print(name + (" has rolled a " + str(rand2)))
    if rand1 > rand2:
        print("Sorry you lose. Thank you for playing.")
    elif rand1 == rand2:
        print(name + " and Aivil have become friends. Thank you for playing.")
    else:
        print("Wow you win!! Thank you for playing.")

#takes you to the caslte for that part of the game
elif ans == 2:
    print("Welcome to the Castle!" + name + " has encountered 2 levers. They are both in the neutral position and" + name + "needs to decide whether or not each lever needs to be pushed forward or pulled backward.")
    print("The levers are labeled with the letters A and B.")
    Lev1 = int(input("For lever A, please input 1 for forward or 2 for backward."))
    Lev2 = int(input("For lever B, please input 1 for forward or 2 for backward."))

    #checking whether you have entered the correct combination.
    if Lev1 == 1 and Lev2 == 2:
        print("Wow! A door opens in front of" + name + "! Prince Leopold was here all along!" + name + "sprinkles him with the potion and he wakes up. He falls in love with" + name + ", immediately and they live happily ever after.")
    elif Lev1 == 2 and (Lev2 == 2 or Lev2 == 1):
        print("Unfortunately, this was the wrong combination and a trap door opens under you!" + name + "falls into the pit never to return... ever again.")
    elif Lev1 == 1 and Lev2 == 1:
        print("Unfortunately, this was the wrong combination and a trap door opens under you!" + name + "falls into the pit never to return... ever again.")
    else:
        print("I’m sorry, please select only 1 or 2. Goodbye.")

#prints an error message if you don't enter one or two
else:
    print("I’m sorry, please select only 1 or 2. Goodbye.")

    
