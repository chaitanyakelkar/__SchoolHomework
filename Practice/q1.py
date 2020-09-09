num = input("Enter a no: ")
no = int(num)
sum = 0
for i in range(0,len(num)):
    sum += (int(num[i]))**3
if sum == no:
    print("it is a armstrong no")
else:
    print("it is a no armstrong no")
