inp = input("Enter a number:")
num = {"0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
for i in inp:
    if i in num:
        j = num.get(i)
        inp = inp.replace(i, j, 1)
print(inp)