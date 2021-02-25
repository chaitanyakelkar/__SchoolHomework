#User input
list_inp = eval(input("Enter the list:"))
for i in range(len(list_inp)):
    if i%2==0 and i + 1 < len(list_inp):
        #temp variable to store even values
        x = list_inp[i]
        list_inp[i] = list_inp[i+1]
    #Using elif instead of else to avoid error in case of odd no items in list
    elif i%2==1:
        list_inp[i] = x
#printing the value
print(list_inp)