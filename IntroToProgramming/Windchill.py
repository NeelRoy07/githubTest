"""
This program calculates the wind chill based on the air temp and the wind speed
Neel, 02/02/22, Period 8
"""

AirTemp = int(input("Enter the air temperature (F): ")) #takes input from the user of the air temp
WindSpeed = int(input("Enter the wind speed (mph): ")) #takes inout from the user of the Wind speed

Windchill = 35.74 + (0.6215 * AirTemp) + ((0.4275 * AirTemp) - 35.75) * (WindSpeed**0.16) #calculates the windchill
print("With an air temperature of " + str(AirTemp) + " and a wind speed of " + str(WindSpeed) + " the windchill is " + str(round(Windchill, 2)) + " degrees (F)")
