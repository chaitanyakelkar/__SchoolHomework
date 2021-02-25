import math
s_b = float(input("Enter side 1"))
s_c = float(input("Enter side 2"))
a_c = math.radians(float(input("Enter angle opposote to side 2")))
a_b = math.degrees(math.asin(s_b*math.sin(a_c)/s_c))
a_a = 180 - a_c - a_b
s_a = s_c*math.sin(math.radians(a_a))/math.sin(math.radians(a_c))
print(f"The third side is {s_a}")
