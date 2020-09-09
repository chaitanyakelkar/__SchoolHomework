no = int(input("Enter a no"))
for i in range(2,no):
    if no%i==0:
        print("its a composite")
        break
    else:
        print("its a prime no")
        break
