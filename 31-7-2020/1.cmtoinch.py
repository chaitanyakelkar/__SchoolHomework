height = int(input("Enter Your Height(cm): "))
if height <= 0:
    print("invalid height")
else:
    h_inch = height / 2.54
    print(f"Your height in inch is {h_inch}")
