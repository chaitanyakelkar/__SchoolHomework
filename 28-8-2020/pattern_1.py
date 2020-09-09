no = 5
for i in range(1, no+1):
    for sp in range(no - i, 0, -1):
        print("  " ,end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(i-1, 0, -1):
        print(k, end=" ")
    print()
for l in range(no-1, 0, -1):
    for sp in range(1, (no - l)+1):
        print("  ",end="")
    for m in range(1, l+1):
        print(m, end=" ")
    for n in range(l-1, 0, -1):
        print(n, end=" ")
    print()
