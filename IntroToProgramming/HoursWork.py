hours = int(input("How many hours did you work this week: "))
hPay = float(input("What is your pay per hour: "))

if hours <= 40:
    pay = hours * hPay

else:
    leftover = hours - 40
    pay = ((hours - leftover) * hPay) + (leftover * (hPay * 1.5))

print("You get "+str(round(pay,2))+" dollars")