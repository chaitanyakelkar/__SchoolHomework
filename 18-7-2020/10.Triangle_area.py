s1 = int(input("enter side 1"))
s2 = int(input("enter side 2"))
s3 = int(input("enter side 3"))
s = (s1+s2+s3)/2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print(f"Area of the triangle is {area}")
