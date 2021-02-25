n = int(input("Enter a number: "))
a, b = 0, 1
print(a,b, sep=",", end=",")
for i in range(1, n-1):
    s = a+b
    if i < n-2:
        print(s, end=",")
        a = b
        b = s
    else:
        print(s)
        a = b
        b = s