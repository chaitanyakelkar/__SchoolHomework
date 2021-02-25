#User Input
a = input("Input :> ")
n = 0
#Logic to check palindrome
for i in range(len(a)//2):
    if a[i] == a[(len(a) - 1 - i)]:
        n += 1
if n == len(a)//2:
    #printing the result
    print("Its a palindrome")
else:
    print("Its is not a palindrome")
a = a.swapcase()
#printing string with inverted case
print(a)