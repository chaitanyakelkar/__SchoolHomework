a = float(input("Enter length 1: "))
b = float(input("Enter length 2: "))
c = float(input("Enter length 3: "))
if (a + b) > c and (b + c) > a and (c + a) > b:
    print("The three sides form a triangle")
else:
    print("The three sides do not form a triangle")
