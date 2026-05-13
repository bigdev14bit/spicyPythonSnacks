print("*" * 70)
print(" Enter Number Of Astericks you want")
print("*" * 70)

userInput = int(input("\nEnter A Number: "))

for index in range(userInput, 0, -1):
    print("1" * index)
