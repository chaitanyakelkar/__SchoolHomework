lst = eval(input("Enter a list of number: "))
swp_num = []

for i in range(1,len(lst),2): 
    swp_num.append(lst[i])       # Numbers at odd index swapped to even
    swp_num.append(lst[i-1])     # Numbers at even index swapped to odd

if lst[-1] not in swp_num:
    swp_num.append(lst[-1])

print("\nSwapped index of numbers:",swp_num)