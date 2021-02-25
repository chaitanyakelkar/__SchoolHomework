inp = input("Enter the string:")
dict1 = {}
for i in inp:
    if i in dict1.keys():
        dict1[i] += 1
    else:
        dict1.setdefault(i,1)
print(dict1)