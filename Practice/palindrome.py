print("This programm checks weather a pattern is a palindrome")
a = input("Input :> ")
n = 0
for i in range(len(a)//2):
    if a[i] == a[(len(a) - 1 - i)]:
        n += 1
if n == len(a)//2:
    print("Its a palindrome")
else:
    print("Its is not a palindrome")