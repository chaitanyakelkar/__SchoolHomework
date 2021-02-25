month = {"JANUARY":31,"FEBRUARY":28,"MARCH":31,"APRIL":30,"MAY":31,"JUNE":30,"JULY":31,"AUGUST":31,"SEPTEMBER":30,"OCTOBER":31,"NOVEMBER":30,"DECEMBER":31}
mon = input("Enter name of month: ").upper()
sorted_dict = {}
sorted_keys = sorted(month, key=month.get)
print(month[mon])
print(sorted(month.keys()))
for i in month:
    if month[i] == 31:
        print(i,end=" ")
for i in sorted_keys:
    sorted_dict[i] = month[i]
print('\n',sorted_dict)