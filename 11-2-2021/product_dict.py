inp = int(input("Enter the number of products you want to store: "))
prod = {}
for i in range(inp):
    print()
    prod.setdefault(input("Enter the prodect name: ") , int(input("Enter the prodect price: ")))
inp2 = int(input("\nEnter the number of prodects you want to query for: "))
for i in range(inp2):
    print()
    prod.get(input("Enter the product name: "), "The product not found")