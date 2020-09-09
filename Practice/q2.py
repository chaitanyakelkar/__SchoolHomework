ch = input("Enter a character: ")
if int(ch) in range(0,9):
    print(ch ,"is a digit")
elif ch=='a' or (ch=='e' or (ch=='i' or (ch=='o' or (ch=='u')))):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")
