# 1. Get user input
# 2. check from the oldest to smallest
age = int(input("Enter age: "))

if age >= 65:
    price = "$8"
elif age >= 13:
    price = "$12"
elif age >= 5:
    price = "$5"
else:
    price = "Free"

print("\nTicket Price:", price)
