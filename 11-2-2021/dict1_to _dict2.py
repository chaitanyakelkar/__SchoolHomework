d1 = {"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
d2 = {}
for i in d1:
    d2.setdefault(i,d1[i][0]+d1[i][1]+d1[i][2])
print(d1,d2,sep="\n")