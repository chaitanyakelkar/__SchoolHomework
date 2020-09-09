no_items = int(input("Enter no of items you purchased: "))
if no_items < 10:
    cost = no_items * 120
elif 10 <= no_items <= 99:
    cost = no_items * 100
else:
    cost = no_items * 70
print(f"Total cost is {cost}")
