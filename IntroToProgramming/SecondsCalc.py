secs = float(input("How many seconds?"))
hours = round(secs/3600)
minutes = round((secs//60) % 60)
RemSecs = round(((secs//60)//60) % 60 )
#round it used to take of the .0 from the line to make the rest look cleaner
print("It is " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(RemSecs) + " seconds.")
