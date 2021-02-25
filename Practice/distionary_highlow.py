#User Input
dictionary = eval(input("Enter the dictionary: "))
#sorting Values
srt = sorted(dictionary.values())
#Printing values
print("Highest number is",srt[-1])
print("Lowest number is",srt[0])