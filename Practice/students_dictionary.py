#User input
dictionary = {}
#variable to store no of students
no = int(input("Enter the number of students: "))
max_marks = 0
for i in range(no):
    name = input("Enter the name of the student: ")
    a = int(input("enter the marks in 1st subject: "))
    b = int(input("Enter the marks in 2nd subject: "))
    c = int(input("Enter the marks in 3rd subject: "))
    dictionary.setdefault(name,[a,b,c,a+b+c])
    if a+b+c > max_marks:
        max_marks = a+b+c
    print()
#Printing the output
print("Highest marks is",max_marks)