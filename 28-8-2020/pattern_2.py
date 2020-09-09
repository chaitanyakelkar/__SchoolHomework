space = 0
for i in range(5, 0, -1):
    print(" " * space, end="")
    space += 2
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(i-1, 0, -1):
        print(k, end=" ")
    print()
space = 6
for l in range(2, 6):
    print(" " * space, end="")
    space -= 2
    for m in range(1, l+1):
        print(m, end=" ")
    for n in range(l-1, 0, -1):
        print(n, end=" ")
    print()
