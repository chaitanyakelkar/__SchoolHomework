#User Input
list_inp = eval(input("Enter the list: "))
count = 0
#Checking if the number is sum of cubes of its digit
for i in list_inp:
    sum_digit = 0
    temp = i
    while temp > 1:
        sum_digit += (temp%10)**3
        temp = temp//10
    if i == sum_digit:
        count += 1
#Printing the output
print("There are",count,"no of items which sum of cubes of their digits")