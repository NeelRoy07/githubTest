Operation = input("What operation do you want to do: Add Subtract Divide Multiply or Power ")
Num1 = float(input("Enter your first number: "))
Num2 = float(input("Enter your second number: ")) 

if Operation.lower() == "add" or Operation == "+":
    Answer = round(Num1 + Num2)
    print("Your answer is: ", round(Answer))

elif Operation.lower() == "subtract" or Operation.lower() =="sub" or Operation =="-":
    print("Your answer is: ", Num1 - Num2)

elif Operation.lower() == "divide" or Operation == "/" or Operation.lower() == "div":
    Answer = Num1 // Num2
    print("Your answer is: ", round(Answer))
 
elif Operation.lower() == "multiply" or Operation == "*":
    Answer = Num1 * Num2
    print("Your answer is: ", round(Answer))

elif Operation.lower() == "power" or Operation.lower() == "square":
    Answer = Num1 ** Num2
    print("Your answer is: ", round(Answer))

else:
    print("Invalid output")