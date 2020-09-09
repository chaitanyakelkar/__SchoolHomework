num = int(input("enter a no: "))
count = 1
while num>1:
    count+=1
    num = num//10
print(f"the no has {count} numbers")
