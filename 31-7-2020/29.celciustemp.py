temperature = float(input("Enter temperature in celcius: "))
if temperature < -273.15:
    print("invalid temprature")
elif temperature == -273.15:
    print("temprature is absolute zero")
elif -273.15 < temperature < 0:
    print("temprature is below freezing")
elif temperature == 0:
    print("temperature is at freezing point")
elif 0 < temperature < 100:
    print("temperature is in  normal range")
elif temperature == 100:
    print("temperature is at boiling point")
else:
    print("temperature is above boiling point")
